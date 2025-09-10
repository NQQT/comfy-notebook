import os

from nofusion.comfy import install_comfy_ui
from nofusion.config import variables

variables({
    # Setting OS
    "root": os.getcwd(),
    # Keys to be used for downloading
    "secret": {
        "civitai": "813701a486b32b80542dd5606dd8efdf"
    }
})

# Installing ComfyUI and all dependencies
install_comfy_ui()
