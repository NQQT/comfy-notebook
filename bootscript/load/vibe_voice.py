import os

from nofusion.comfy import fetch_custom_node

# Standard Comfy File Setup
package_dir = os.path.dirname(__file__)
# Setting up the minimum requirements
common_script = os.path.join(package_dir, '../common.py')
# Running common file first
with open(common_script, "r") as file:
    exec(file.read())

# Required Vibe Voice
fetch_custom_node("https://github.com/wildminder/ComfyUI-VibeVoice/")
