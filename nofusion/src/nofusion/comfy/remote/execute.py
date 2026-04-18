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

    last_uploaded: dict[str, bytes] = {}

    while True:
        try:
            available_files = db_master.list()
            if available_files is None:
                print(f"[slave:{name}] db_master.list() failed — skipping...")
                await asyncio.sleep(random.uniform(5.0, 10.0))
                continue

            # Find all files matching workflow*.json and pick the latest by updated timestamp
            workflow_files = [
                f for f in available_files
                if f["filename"].startswith("workflow") and f["filename"].endswith(".json")
            ]

            if not workflow_files:
                log_idle("pending")
                print(f"[slave:{name}] No workflow*.json found — sleeping...")
                await asyncio.sleep(random.uniform(5.0, 10.0))
                continue

            latest_workflow_file = max(
                workflow_files,
                key=lambda f: datetime.fromisoformat(f["updated"].rstrip("Z")),
            )
            latest_workflow_name = latest_workflow_file["filename"]
            print(
                f"[slave:{name}] Using latest workflow file: {latest_workflow_name} (updated: {latest_workflow_file['updated']})")

            # TODO latest_workflow_file["checksum"] should be check. If it is the same previously
            #  There is no need to call "json_string = db_master.get(latest_workflow_name)" again, just load cached one

            json_string = db_master.get(latest_workflow_name)
            if json_string is None:
                print(f"[slave:{name}] db_master.get('{latest_workflow_name}') failed — skipping...")
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

            if results is None:
                print(f"[slave:{name}] run_with_log_monitor returned None — skipping upload...")
                log_idle()
                continue

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            for filename, image_data in results.items():
                if last_uploaded.get(filename) == image_data:
                    print(f"[slave:{name}] Skipping duplicate image: {filename}")
                    continue

                stamped_name = f"{timestamp}_{filename}"

                push_result = db_storage.push(f"{stamped_name}.shard", {
                    "data": base64.b64encode(image_data).decode("utf-8"),
                })
                if push_result is None:
                    print(f"[slave:{name}] db_storage.push() failed for {stamped_name} — skipping...")
                    continue

                last_uploaded[filename] = image_data

            log_idle()

        except Exception as e:
            print(f"[slave:{name}] Error during iteration: {e}")
            await asyncio.sleep(random.uniform(5.0, 10.0))
