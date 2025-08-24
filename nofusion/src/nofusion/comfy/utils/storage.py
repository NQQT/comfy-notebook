from noobish.core import path_remove, path_symbolic_create
from ..location import location_ipadaptor, location_checkpoints, location_diffusion_models, location_clip, \
    location_clip_vision, location_text_encoders, location_vae, location_unet
from ...shell import shell_command


# This is design to create temporary storage
# Some cloud has no persistence storage, or it is expensive
def storage_temporary():
    # Creating Temporary Folders
    shell_command(
        "mkdir /tmp/models",
        "mkdir /tmp/models/checkpoints",
        "mkdir /tmp/models/diffusion_models",
        "mkdir /tmp/models/clip",
        "mkdir /tmp/models/clip_vision",
        "mkdir /tmp/models/ipadapter",
        "mkdir /tmp/models/text_encoders",
        "mkdir /tmp/models/vae",
        "mkdir /tmp/models/unet"
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
    path_symbolic_create("/tmp/models/clip_vision", location_clip_vision())
    path_symbolic_create("/tmp/models/ipadapter", location_ipadaptor())
    path_symbolic_create("/tmp/models/text_encoders", location_text_encoders())
    path_symbolic_create("/tmp/models/vae", location_vae())
    path_symbolic_create("/tmp/models/unet", location_unet())
