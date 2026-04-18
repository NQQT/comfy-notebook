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
    from comfy_api_simplified import ComfyApiWrapper

    api = ComfyApiWrapper("http://127.0.0.1:8188")
    stash_id = variables("stash")
    name = variables("name.agent")

    db_master = Database(stash_id)
    db_storage = Database(f"{stash_id}_stash")

    print(f"[slave:{name}] Starting. Watching bin: {stash_id}")

    # Track last uploaded data per filename to deduplicate uploads.
    # Keyed by filename, stores the raw bytes of the last pushed image.
    # Persists across loop iterations so the same workflow.json re-run
    # won't re-upload an image that hasn't changed.
    last_uploaded: dict[str, bytes] = {}

    while True:
        try:
            # db_master.list() may return None on failure — skip iteration
            available_files = db_master.list()
            if available_files is None:
                print(f"[slave:{name}] db_master.list() failed — skipping...")
                await asyncio.sleep(random.uniform(5.0, 10.0))
                continue

            if not any(f["filename"] == "workflow.json" for f in available_files):
                log_idle("pending")
                print(f"[slave:{name}] workflow.json not found — sleeping...")
                await asyncio.sleep(random.uniform(5.0, 10.0))
                continue

            # db_master.get() may return None on failure — skip iteration
            json_string = db_master.get("workflow.json")
            if json_string is None:
                print(f"[slave:{name}] db_master.get('workflow.json') failed — skipping...")
                await asyncio.sleep(random.uniform(5.0, 10.0))
                continue

            workflow = json_string if isinstance(json_string, dict) else json.loads(json_string)

            log_busy("processing")

            results = await run_with_log_monitor(
                api,
                workflow,
                output_node="Save Image",
                log_path=f"{variables('root')}/comfyui_stderr.log",
                poll_interval=2.0,
            )

            # run_with_log_monitor may theoretically return None — guard against it
            if results is None:
                print(f"[slave:{name}] run_with_log_monitor returned None — skipping upload...")
                log_idle()
                continue

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            for filename, image_data in results.items():
                # Skip upload if this exact image was the last one uploaded
                # for this filename — handles A,A sequences.
                # A,B,A is still fully uploaded because last_uploaded[filename]
                # will be A after the first, then B after the second, so the
                # third (A again) differs from the stored B and gets pushed.
                if last_uploaded.get(filename) == image_data:
                    print(f"[slave:{name}] Skipping duplicate image: {filename}")
                    continue

                stamped_name = f"{timestamp}_{filename}"

                # db_storage.push() may return None on failure — skip this
                # file but continue processing remaining results
                push_result = db_storage.push(f"{stamped_name}.shard", {
                    "data": base64.b64encode(image_data).decode("utf-8"),
                })
                if push_result is None:
                    print(f"[slave:{name}] db_storage.push() failed for {stamped_name} — skipping...")
                    continue

                # Update the tracker only after a successful push
                last_uploaded[filename] = image_data

            log_idle()

        except Exception as e:
            print(f"[slave:{name}] Error during iteration: {e}")
            await asyncio.sleep(random.uniform(5.0, 10.0))
