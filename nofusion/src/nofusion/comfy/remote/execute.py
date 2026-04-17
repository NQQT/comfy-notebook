import threading
import time

from comfy_api_simplified import ComfyApi
from noobish.web import FileBin


async def run_with_log_monitor(api, name, workflow, output_node, log_path, poll_interval=2.0):
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


import asyncio
import json
import random
import string
from datetime import datetime


def _random_name(length=8) -> str:
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


async def start_comfy_ui_slave(bin_location="kaggle_test", poll_interval: float = 5.0):
    api = ComfyApi("http://127.0.0.1:8188")
    name = _random_name()

    filebin_master = FileBin(bin_location)
    filebin_storage = FileBin(f"{bin_location}_stash")

    print(f"[slave:{name}] Starting. Watching bin: {bin_location}")

    while True:
        try:
            # Refresh the file listing from the master bin
            available_files = filebin_master.list()

            # If no work is queued, wait before checking again
            if "workflow.json" not in available_files:
                print(f"[slave:{name}] workflow.json not found — sleeping...")
                await asyncio.sleep(random.uniform(5.0, 10.0))
                continue

            # --- Workflow found: proceed immediately, no sleep ---

            # Download and parse the workflow
            json_string = filebin_master.download("workflow.json")
            workflow = json.loads(json_string)

            # Announce this slave is alive and working
            status = {
                "name": name,
                "status": "running",
                "timestamp": datetime.now().isoformat(),
            }
            filebin_master.upload(status, f"slave_{name}.json")

            # Run the workflow
            results = await run_with_log_monitor(
                api,
                name,
                workflow,
                output_node="Save Image",
                log_path="/kaggle/working/comfyui_stderr.log",
                poll_interval=2.0,
            )

            # Upload results to storage bin
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            for filename, image_data in results.items():
                stamped_name = f"{timestamp}_{filename}"
                filebin_storage.upload(image_data, f"{stamped_name}.png")
                print(f"[slave:{name}] Saved: {stamped_name}.png")

            # Mark as idle after completing a run
            status["status"] = "idle"
            status["last_run"] = timestamp
            filebin_master.upload(status, f"slave_{name}.json")

            # Loop back immediately — pick up next workflow.json if already queued

        except Exception as e:
            print(f"[slave:{name}] Error during iteration: {e}")
            # Brief backoff on error to avoid tight crash-loops
            await asyncio.sleep(random.uniform(5.0, 10.0))
