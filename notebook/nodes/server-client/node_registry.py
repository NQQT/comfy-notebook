from .nodes.client.ClientImageSaveNode import ImageSaveNode
from .nodes.client.ClientVideoSaveNode import VideoSaveNode
from .nodes.memory import MemoryImageNode

# Node Registration for ComfyUI
NODE_CLASS_MAPPINGS = {
    "ClientImageDownloadNode": ImageSaveNode,
    "ClientVideoDownloadNode": VideoSaveNode,

    "ServerMemoryImageNode":MemoryImageNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ClientImageDownloadNode": "Client Image Download",
    "ClientVideoDownloadNode": "Client Video Download",

    "ServerMemoryImageNode":"Server Memory Image Node"
}