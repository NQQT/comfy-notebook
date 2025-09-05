from nofusion.comfy import install_comfy_ui
from nofusion.config import variables

variables({
    # Require to define the correct root for kaggle
    "root": "/root"
})

# Installing ComfyUI
install_comfy_ui()
