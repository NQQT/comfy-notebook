import os

from nofusion.source import source_model_wan_i2v, source_wan_i2v_lightning_loras, \
    source_wan_i2v_nsfw_loras

# Standard Comfy File Setup
package_dir = os.path.dirname(__file__)
# Setting up the minimum requirements
common_script = os.path.join(package_dir, '../common.py')
# Running common file first
with open(common_script, "r") as file:
    exec(file.read())

# Only Q6 can fit right now
source_model_wan_i2v()
source_wan_i2v_lightning_loras()
source_wan_i2v_nsfw_loras()
