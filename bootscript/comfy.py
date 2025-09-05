import os

from IPython.core.display_functions import clear_output

from nofusion.comfy import install_comfy_ui
from nofusion.config import variables
from nofusion.source import source_model_pony_cyber_realistic, source_model_wan_i2v, source_wan_i2v_lightning_loras, \
    source_wan_i2v_nsfw_loras

variables({
    # Setting OS
    "root": os.getcwd()
})

# Installing ComfyUI and all dependencies
install_comfy_ui()

# Setting up Cyber realistic
source_model_pony_cyber_realistic()

# Only Q6 can fit right now
source_model_wan_i2v("14B_Q5_K_M")
source_wan_i2v_lightning_loras()
source_wan_i2v_nsfw_loras()
clear_output()
