import os

from nofusion.comfy import install_comfy_ui
from nofusion.config import variables
from nofusion.source import source_model_pony_cyber_realistic, source_model_wan_i2v, source_wan_i2v_lightning_loras, \
    source_wan_i2v_nsfw_loras

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

# Setting up Cyber realistic
source_model_pony_cyber_realistic()

# Only Q6 can fit right now
source_model_wan_i2v("14B_Q5_K_M")
source_wan_i2v_lightning_loras()
source_wan_i2v_nsfw_loras()
