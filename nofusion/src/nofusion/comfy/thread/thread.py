import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request

from ..config import variables


def start_comfy_ui_thread(host="127.0.0.1", port=8188):
    root_dir = variables('root')

    # Single combined log file is sufficient — process either runs or dies
    log_path = f"{root_dir}/comfyui.log"
    log_file = open(log_path, "w")

    comfy_ui = variables('name.comfy')
    proc_holder = {}

    def _run():
        try:
            proc = subprocess.Popen(
                [sys.executable, "main.py", "--listen", host, "--port", str(port)],
                cwd=f"{root_dir}/{comfy_ui}",
                stdout=log_file,
                stderr=log_file,  # Merge stderr into the same file
            )
            proc_holder["proc"] = proc
            proc.wait()
        except Exception as e:
            # Write the exception itself into the log so it's captured
            log_file.write(f"\n[FATAL] Failed to start ComfyUI: {e}\n")
            import traceback
            log_file.write(traceback.format_exc())
        finally:
            log_file.flush()
            log_file.close()

    def stop():
        proc = proc_holder.get("proc")
        if proc and proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()

    thread = threading.Thread(target=_run, name="comfyui-server", daemon=True)
    thread.start()

    return thread, stop


def wait_for_comfyui(
        host="127.0.0.1",
        port=8188,
        timeout=120,
        interval=2,
        log_path: str | None = None,
):
    """Poll ComfyUI's /queue endpoint until it responds or timeout is reached.

    On timeout, dumps the ComfyUI log (if log_path is provided or can be
    inferred from variables) so the caller can diagnose the failure.
    """
    url = f"http://{host}:{port}/queue"
    deadline = time.time() + timeout
    print(f"Waiting for ComfyUI to start at {url}...")

    # Resolve log path lazily so this function stays usable in isolation
    if log_path is None:
        root_dir = variables("root")
        log_path = f"{root_dir}/comfyui.log"

    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=3) as resp:
                if resp.status == 200:
                    print("ComfyUI is ready!")
                    return True
        except (urllib.error.URLError, ConnectionRefusedError, OSError):
            pass  # Not up yet
        time.sleep(interval)

    # ── Timeout reached: dump the log before raising ──────────────────────────
    log_contents = _read_log(log_path)
    raise TimeoutError(
        f"ComfyUI did not start within {timeout} seconds.\n"
        f"── ComfyUI log ({log_path}) ─────────────────────────────────────\n"
        f"{log_contents}"
        f"\n─────────────────────────────────────────────────────────────────"
    )


def _read_log(log_path: str, tail_lines: int = 100) -> str:
    """Return the last *tail_lines* lines of *log_path*, or a helpful message."""
    try:
        with open(log_path, "r", errors="replace") as f:
            lines = f.readlines()
        if not lines:
            return "(log file is empty)"
        # Tail the log so the exception message stays manageable
        trimmed = lines[-tail_lines:]
        prefix = f"(showing last {tail_lines} of {len(lines)} lines)\n" if len(lines) > tail_lines else ""
        return prefix + "".join(trimmed)
    except FileNotFoundError:
        return f"(log file not found: {log_path})"
    except OSError as e:
        return f"(could not read log: {e})"


# For initiating comfyUI
def initiate_comfy_ui_thread():
    # Starting ComfyUI
    thread, stop_server = start_comfy_ui_thread()
    wait_for_comfyui()
