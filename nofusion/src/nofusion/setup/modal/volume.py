# For Setting up Cyber Realistic
import os

from ...config import variables
from ...shell import shell_command


# For setting up modal volume
def setup_modal_volume(volume_name: str):
    # Checking volume already exists
    volume_path = f"/mnt/{volume_name}"
    if not os.path.exists(volume_path):
        # Creating a Volume
        shell_command(f"modal volume create {volume_name}")

    # Reconfiguring Variables
    variables({
        # Updating Root Path
        "root": volume_path
    })


# For Creating Modal volume
def setup_modal_volume_assets(volume_name: str):
    # Creating a Volume
    setup_modal_volume(volume_name)
    dir_models = f"/mnt/{volume_name}/models"

    # Making the Model Directory
    os.mkdir(dir_models)

    # Updating Variables
    variables({
        # Updating Root Path
        "dir": {
            "models": dir_models
        }
    })
