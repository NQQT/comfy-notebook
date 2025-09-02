import os

from .config import configure_variables
from .location import location_ipadaptor
from .utils import fetch_custom_node
from ..config import variables
from ..install import install_package
from ..shell import shell_command


# For installing comfy UI
def install_comfy_ui(checkout_version="e2d1e5dad98dbbcf505703ea8663f20101e6570a"):
    # Configuring Variables
    configure_variables()

    # Getting the variables
    root_dir = variables("root")
    comfy_name = variables("name.comfy")

    os.chdir(root_dir)
    # Executing Shell Commands
    # Cloning Comfy UI
    shell_command(f"git clone https://github.com/comfyanonymous/ComfyUI.git {comfy_name}")

    os.chdir(f"{root_dir}/{comfy_name}")
    shell_command(f"git checkout {checkout_version}")

    pip = variables("pip")

    # Installing the necessary requirements
    shell_command(f"{pip} install -r requirements.txt")

    # Creating Temporary Folder
    shell_command(
        # Require the ip-adapter Folder
        f"mkdir {location_ipadaptor()}"
    )

    # Download Comfy UI Manager
    fetch_custom_node("https://github.com/Comfy-Org/ComfyUI-Manager")

    # Additional installation to use
    install_package(
        "pillow==10.2.0",
        "insightface",
        "onnxruntime",
        "onnxruntime-gpu",
        "matplotlib-inline"
    )

    # For installing custom nodes
    fetch_custom_node("https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite")
    fetch_custom_node("https://github.com/kijai/ComfyUI-KJNodes")
    # git_custom_node("https://github.com/yolain/ComfyUI-Easy-Use","717092a3ceb51c474b5b3f77fc188979f0db9d67")
    fetch_custom_node("https://github.com/rgthree/rgthree-comfy")
    # RES_2S Sampler (better and sharper)
    fetch_custom_node("https://github.com/ClownsharkBatwing/RES4LYF")
    # for loading GGUF model
    fetch_custom_node("https://github.com/city96/ComfyUI-GGUF")
    # for multi GPU
    fetch_custom_node("https://github.com/pollockjj/ComfyUI-MultiGPU")
    fetch_custom_node("https://github.com/skyiron/ComfyUI-DistributedGPU")
    # for interpolation
    fetch_custom_node("https://github.com/kijai/ComfyUI-GIMM-VFI")
    # For running Cloud Based ComfyUI with Local Controls
    fetch_custom_node("https://github.com/comfyscript/ComfyUI-CloudClient")
    # For Upscaling and so on
    fetch_custom_node("https://github.com/kijai/ComfyUI-SUPIR")
