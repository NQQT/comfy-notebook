import os

from nofusion.source import source_model_qwen_edit, source_lora_qwen_edit_useful

# Standard Comfy File Setup
package_dir = os.path.dirname(__file__)
# Setting up the minimum requirements
common_script = os.path.join(package_dir, '../common.py')
# Running common file first
with open(common_script, "r") as file:
    exec(file.read())

# Qwen Image Edit
source_model_qwen_edit()
source_lora_qwen_edit_useful()
