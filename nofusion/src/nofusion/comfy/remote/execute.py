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
    bin_id = variables("bin")
    name = variables("name.agent")

    db_master = Database(bin_id)
    stash_id = "temporary"

    print(f"[slave:{name}] Starting. Watching bin: {bin_id}")

    last_uploaded: dict[str, bytes] = {}
    cached_workflow: dict | None = None
    cached_workflow_checksum: str | None = None

    # Persistent counter for successfully saved images across the run lifetime.
    # This makes shard names deterministic and monotonically increasing,
    # unlike timestamps which can collide or vary across restarts.
    saved_image_count = 0

    while True:
        try:
            available_files = db_master.list()
            if available_files is None:
                print(f"[slave:{name}] db_master.list() failed — skipping...")
                await asyncio.sleep(random.uniform(5.0, 10.0))
                continue

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
                f"[slave:{name}] Using latest workflow file: {latest_workflow_name} "
                f"(updated: {latest_workflow_file['updated']})"
            )

            parts = latest_workflow_name.removesuffix(".json").split("_")
            if len(parts) >= 2:
                stash_id = parts[-1]
            else:
                print(
                    f"[slave:{name}] WARNING: Could not extract stash_id from "
                    f"'{latest_workflow_name}', using fallback."
                )
                stash_id = "temporary"

            current_checksum = latest_workflow_file.get("checksum")
            if current_checksum and current_checksum == cached_workflow_checksum and cached_workflow is not None:
                print(f"[slave:{name}] Checksum unchanged ({current_checksum[:8]}…) — using cached workflow.")
                workflow = cached_workflow
            else:
                json_string = db_master.get(latest_workflow_name)
                if json_string is None:
                    print(f"[slave:{name}] db_master.get('{latest_workflow_name}') failed — skipping...")
                    await asyncio.sleep(random.uniform(5.0, 10.0))
                    continue

                workflow = json_string if isinstance(json_string, dict) else json.loads(json_string)
                cached_workflow = workflow
                cached_workflow_checksum = current_checksum
                print(f"[slave:{name}] Fetched and cached workflow (checksum: {current_checksum}).")

            log_busy("processing")

            # Use the saved image counter as the unique_id.
            # Zero-padded to 6 digits so lexicographic and numeric sort order agree.
            unique_id = f"{saved_image_count:06d}"
            stamped_name = f"{name}_{unique_id}.shard"

            Database(f"{bin_id}_{stash_id}").push(stamped_name, {
                "status": "pending",
                "data": ""
            })

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

            for filename, image_data in results.items():
                if last_uploaded.get(filename) == image_data:
                    print(f"[slave:{name}] Skipping duplicate image: {filename}")
                    continue

                push_result = Database(f"{bin_id}_{stash_id}").push(stamped_name, {
                    "status": "completed",
                    "data": base64.b64encode(image_data).decode("utf-8"),
                })

                if push_result is None:
                    print(f"[slave:{name}] db_storage.push() failed for {stamped_name} — skipping...")
                    continue

                last_uploaded[filename] = image_data
                # Increment only on confirmed successful cloud save
                saved_image_count += 1
                print(f"[slave:{name}] Saved image #{saved_image_count} as {stamped_name}")

            log_idle()

        except Exception as e:
            print(f"[slave:{name}] Error during iteration: {e}")
            await asyncio.sleep(random.uniform(5.0, 10.0))
