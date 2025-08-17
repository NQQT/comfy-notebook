from noobish.core import path_remove, path_symbolic_create
from .config import configure_variables
from .location import location_ipadaptor, location_checkpoints, location_diffusion_models, location_clip, \
    location_clip_vision, location_text_encoders, location_vae, location_unet
from ..config import variables
from ..shell import shell_command


# For installing comfy UI
def install_comfy_ui(checkout_version="37d620a6b85f61b824363ed8170db373726ca45a"):
    # Configuring Variables
    configure_variables()

    # Getting the variables
    root_dir = variables("root")
    comfy_name = variables("name.comfy")

    # Executing Shell Commands
    shell_command(
        # Go back to the main root directory
        f"cd {root_dir}",
        # Cloning Comfy UI
        f"git clone https://github.com/comfyanonymous/ComfyUI.git {comfy_name}",
        f"cd {comfy_name}",
        f"git checkout {checkout_version}",
    )

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

    # Additional installation to use
    # !{pip} install pillow==10.2.0 insightface onnxruntime onnxruntime-gpu
    # !{pip} install matplotlib-inline
