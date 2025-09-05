import os

from nofusion.comfy import install_comfy_ui
from nofusion.config import variables

variables({
    # Setting OS
    "root": os.getcwd()
})

# Installing ComfyUI and all dependencies
install_comfy_ui()
