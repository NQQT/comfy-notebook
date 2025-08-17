from ..config import variables


def location_comfy_ui():
    return f"{variables('root')}/{variables('name.comfy')}"


# Return the location of the custom nodes
def location_custom_nodes():
    return f"{location_comfy_ui()}/custom_nodes"


def location_models():
    return f"{location_comfy_ui()}/models"


def location_ipadaptor():
    return f"{location_models()}/ipadapter"


def location_checkpoints():
    return f"{location_models()}/checkpoints"


def location_diffusion_models():
    return f"{location_models()}/diffusion_models"


def location_clip():
    return f"{location_models()}/clip"


def location_clip_vision():
    return f"{location_models()}/clip_vision"


def location_text_encoders():
    return f"{location_models()}/text_encoders"


def location_vae():
    return f"{location_models()}/vae"


def location_unet():
    return f"{location_models()}/unet"
