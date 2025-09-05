import os

from ..config import variables
from ...shell import shell_command


# For starting a piggy tunnel
def start_pinggy_tunnel(args=""):
    package_dir = os.path.dirname(__file__)
    # Setting up the minimum requirements
    pingy_script = os.path.join(package_dir, 'pinggy.py')

    python = variables('python')
    root_dir = variables('root')
    comfy_ui = variables('name.comfy')
    # For Running ComfyUI
    os.chdir(root_dir)

    # Running Command
    shell_command(f"{python} {pingy_script} --command='{python} {root_dir}/{comfy_ui}/main.py {args}' --port=8188")
