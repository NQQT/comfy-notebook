import os

from noobish.core import path_remove, path_symbolic_create
from .config import configure_variables
from .location import location_ipadaptor, location_checkpoints, location_diffusion_models, location_clip, \
    location_clip_vision, location_text_encoders, location_vae, location_unet
from .preset.nodes import nodes_symbolic_import
from .utils import fetch_custom_node
from ..config import variables
from ..install import install_package
from ..shell import shell_command


# For installing comfy UI
def install_comfy_ui(checkout_version="da2efeaec6609265051165bfb413a2a4c84cf4bb"):
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
        "mkdir /tmp/models",
        "mkdir /tmp/models/checkpoints",
        "mkdir /tmp/models/diffusion_models",
        "mkdir /tmp/models/clip",
        "mkdir /tmp/models/clip_vision",
        "mkdir /tmp/models/ipadapter",
        "mkdir /tmp/models/text_encoders",
        "mkdir /tmp/models/vae",
        "mkdir /tmp/models/unet",
        # Require the ip-adapter Folder
        f"mkdir {location_ipadaptor()}",
    )

    # Remove all these paths
    path_remove(
        location_checkpoints(),
        location_diffusion_models(),
        location_clip(),
        location_clip_vision(),
        location_ipadaptor(),
        location_text_encoders(),
        location_vae(),
        location_unet()
    )

    path_symbolic_create("/tmp/models/checkpoints", location_checkpoints())
    path_symbolic_create("/tmp/models/diffusion_models", location_diffusion_models())
    path_symbolic_create("/tmp/models/clip", location_clip())
    path_symbolic_create("/tmp/models/clip_vision", location_clip())
    path_symbolic_create("/tmp/models/ipadapter", location_ipadaptor())
    path_symbolic_create("/tmp/models/text_encoders", location_text_encoders())
    path_symbolic_create("/tmp/models/vae", location_vae())
    path_symbolic_create("/tmp/models/unet", location_unet())

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
    # for loading GGUF model
    fetch_custom_node("https://github.com/city96/ComfyUI-GGUF")
    # for multi GPU
    fetch_custom_node("https://github.com/pollockjj/ComfyUI-MultiGPU")
    # for interpolation
    # git_custom_node("https://github.com/Fannovel16/ComfyUI-Frame-Interpolation")
    fetch_custom_node("https://github.com/kijai/ComfyUI-GIMM-VFI")

    # Installing custom nodes
    nodes_symbolic_import(f"{root_dir}/comfy-notebook/nodes")
