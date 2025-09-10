import os

from nofusion.source import source_model_pony_cyber_realistic

# Standard Comfy File Setup
package_dir = os.path.dirname(__file__)
# Setting up the minimum requirements
common_script = os.path.join(package_dir, '../common.py')
# Running common file first
with open(common_script, "r") as file:
    exec(file.read())

# Setting up Cyber realistic
source_model_pony_cyber_realistic()
