from .nodes.LocalImageSaveNode import ImageSaveNode

# Node Registration for ComfyUI
NODE_CLASS_MAPPINGS = {
    "LocalImageSaveNode": ImageSaveNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LocalImageSaveNode": "Local Image Save"
}