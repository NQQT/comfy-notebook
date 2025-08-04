from .nodes.ClientImageSaveNode import ImageSaveNode
from .nodes.ClientVideoSaveNode import VideoSaveNode

# Node Registration for ComfyUI
NODE_CLASS_MAPPINGS = {
    "ClientImageSaveNode": ImageSaveNode,
    "ClientVideoSaveNode": VideoSaveNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ClientImageSaveNode": "Client Image Save",
    "ClientVideoSaveNode": "Client Video Save"
}