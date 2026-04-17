from nofusion.comfy import shell_command
from nofusion.config import variables

script = """

import threading
import subprocess
import sys
from nofusion.config import variables
from nofusion.comfy import configure_variables
variables({
    # Define the cloud environment for optimisation
    "cloud": "kaggle",
    # Use Coda Version 118
    "cuda": "118",
    # Require to define the correct root for kaggle
    "root": "/kaggle/working",

    # Keys to be used for downloading
    "secret": {
        "civitai": "813701a486b32b80542dd5606dd8efdf"
    }
})

def start_comfyui_server(host="127.0.0.1", port=8188):
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

    thread = threading.Thread(target=_run, name="comfyui-server", daemon=True)
    thread.start()
    return thread, stop


thread, stop_server = start_comfyui_server()




# Auto-kill after 30 seconds (non-blocking, like JS setTimeout)
timer = threading.Timer(120, stop_server)
timer.start()

"""

import threading


def _run_test():
    with open("/kaggle/working/test.py", "w") as f:
        f.write(script)

    python = variables('python')
    root_dir = variables('root')
    comfy_ui = variables('name.comfy')

    shell_command(f"{python} test.py")


t = threading.Thread(target=_run_test, daemon=True)
t.start()
