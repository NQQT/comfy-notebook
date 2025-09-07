import subprocess

import psutil

# Kill existing ComfyUI subprocesses with main.py in the command line:
for proc in psutil.process_iter(['pid', 'cmdline']):
    try:
        cmdline = proc.info['cmdline']
        if cmdline and 'ComfyUI/main.py' in ' '.join(cmdline):
            print(f"Terminating existing ComfyUI subprocess with PID: {proc.pid}")
            proc.terminate()
            proc.wait(timeout=5)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

# Start new ComfyUI subprocess
command = [
    "python3",
    "ComfyUI/main.py",
    "--listen",
    "--port=8888",
    "--tls-keyfile", "key.pem",
    "--tls-certfile", "cert.pem"
]

process = subprocess.Popen(command)
print(f"Started ComfyUI subprocess with PID: {process.pid}")
