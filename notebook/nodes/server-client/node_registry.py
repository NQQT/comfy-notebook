from .nodes.ClientImageSaveNode import ImageSaveNode
from .nodes.ClientMp4VideoSaveNode import Mp4VideoSaveNode
from .nodes.ClientVideoSaveNode import VideoSaveNode

# Node Registration for ComfyUI
NODE_CLASS_MAPPINGS = {
    "ClientImageSaveNode": ImageSaveNode,
    "ClientVideoSaveNode": VideoSaveNode,

    # Experimental
    "ClientMp4VideoSaveNode": Mp4VideoSaveNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ClientImageSaveNode": "Client Image Download",
    "ClientVideoSaveNode": "Client Video Download",

    # Experimental
    "ClientMp4VideoSaveNode": "Client Mp4 Video Download",
}