import os

from nofusion.source import source_model_pony_cyber_realistic, civitai_fetch_loras

# Standard Comfy File Setup
package_dir = os.path.dirname(__file__)
# Setting up the minimum requirements
common_script = os.path.join(package_dir, '../common.py')
# Running common file first
with open(common_script, "r") as file:
    exec(file.read())

# Setting up Cyber realistic
source_model_pony_cyber_realistic()
# For Illustrious
civitai_fetch_loras("pony_beauty_slider", "518458")
civitai_fetch_loras("pony_char_seo_baek_hyang", "697834")
civitai_fetch_loras("pony_expressive_h", "382152")
