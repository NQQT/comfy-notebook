import asyncio
import base64
import json
import random
import threading
import time
from datetime import datetime

from noobish.web import Database

from .logging import log_busy, log_idle
from ..config import variables


# This allows to run log monitoring
async def run_with_log_monitor(api, workflow, output_node, log_path, poll_interval=2.0):
    loop = asyncio.get_event_loop()
    stop_event = threading.Event()

    def log_monitor():
        last_pos = 0
        while not stop_event.is_set():
            try:
                with open(log_path, "r") as f:
                    f.seek(last_pos)
                    new_content = f.read()
                    if new_content:
                        print(new_content, end="", flush=True)
                    last_pos = f.tell()
            except FileNotFoundError:
                pass
            time.sleep(poll_interval)

        # Final flush
        try:
            with open(log_path, "r") as f:
                f.seek(last_pos)
                remainder = f.read()
                if remainder:
                    print(remainder, end="", flush=True)
        except FileNotFoundError:
            pass

    monitor_thread = threading.Thread(target=log_monitor, daemon=True)
    monitor_thread.start()

    try:
        results = await loop.run_in_executor(
            None, api.queue_and_wait_images, workflow, output_node
        )
    finally:
        stop_event.set()
        monitor_thread.join(timeout=poll_interval + 1)

    return results


async def start_comfy_ui_slave(poll_interval: float = 5.0):
    from comfy_api_simplified import ComfyApi
    
    api = ComfyApi("http://127.0.0.1:8188")
    stash_id = variables("stash")
    name = variables("name")

    # Master is controlled by the user
    db_master = Database(stash_id)
    # Stash to store data
    db_storage = Database(f"{stash_id}_stash")

    print(f"[slave:{name}] Starting. Watching bin: {stash_id}")

    while True:
        try:
            # Refresh the file listing from the master bin
            available_files = db_master.list()

            # If no work is queued, wait before checking again
            if "workflow.json" not in available_files:
                # Waiting for workflow.json
                log_idle("pending")

                print(f"[slave:{name}] workflow.json not found — sleeping...")
                await asyncio.sleep(random.uniform(5.0, 10.0))
                continue

            # --- Workflow found: proceed immediately, no sleep ---

            # Download and parse the workflow
            json_string = db_master.get("workflow.json")
            workflow = json.loads(json_string)

            # Announce this slave is alive and working
            log_busy("processing")

            # Run the workflow
            results = await run_with_log_monitor(
                api,
                workflow,
                output_node="Save Image",
                log_path=f"{variables("root")}/comfyui_stderr.log",
                poll_interval=2.0,
            )

            # Upload results to storage bin
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Scan through the list of items and save it
            for filename, image_data in results.items():
                # This is just a name
                stamped_name = f"{timestamp}_{filename}"

                # Uploading the file
                db_storage.push(f"{stamped_name}.shard", {
                    "data": base64.b64encode(image_data).decode("utf-8"),
                })

            # Idle now
            log_idle()

            # Loop back immediately — pick up next workflow.json if already queued

        except Exception as e:
            print(f"[slave:{name}] Error during iteration: {e}")
            # Brief backoff on error to avoid tight crash-loops
            await asyncio.sleep(random.uniform(5.0, 10.0))
