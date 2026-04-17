import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request

from ..config import variables


# For starting up a comfi you thread
def start_comfy_ui_thread(host="127.0.0.1", port=8188):
    root_dir = variables('root')
    comfy_ui = variables('name.comfy')
    proc_holder = {}

    log_stdout = open(f"{root_dir}/comfyui_stdout.log", "w")
    log_stderr = open(f"{root_dir}/comfyui_stderr.log", "w")

    def _run():
        proc = subprocess.Popen(
            [sys.executable, "main.py", "--listen", host, "--port", str(port)],
            cwd=f"{root_dir}/{comfy_ui}",
            stdout=log_stdout,
            stderr=log_stderr,
        )
        proc_holder["proc"] = proc
        proc.wait()

        # Close all the logs
        log_stdout.close()
        log_stderr.close()

    def stop():
        proc = proc_holder.get("proc")
        if proc and proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()

    # Starting the thread
    thread = threading.Thread(target=_run, name="comfyui-server", daemon=True)
    thread.start()

    # Returning the thread
    return thread, stop


def wait_for_comfyui(host="127.0.0.1", port=8188, timeout=120, interval=2):
    """Poll ComfyUI's /queue endpoint until it responds or timeout is reached."""
    url = f"http://{host}:{port}/queue"
    deadline = time.time() + timeout
    print(f"Waiting for ComfyUI to start at {url}...")
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=3) as resp:
                if resp.status == 200:
                    print("ComfyUI is ready!")
                    return True
        except (urllib.error.URLError, ConnectionRefusedError, OSError):
            pass  # Not up yet
        time.sleep(interval)
    raise TimeoutError(f"ComfyUI did not start within {timeout} seconds.")


# This is to start the comfy ui thread
def initiate_comfy_ui_thread():
    thread, stop_server = start_comfy_ui_thread()

    # # Auto-kill after 30 seconds (non-blocking, like JS setTimeout)
    # timer = threading.Timer(30, stop_server)
    # timer.start()

    # Wait for it completely run
    wait_for_comfyui(timeout=120)
