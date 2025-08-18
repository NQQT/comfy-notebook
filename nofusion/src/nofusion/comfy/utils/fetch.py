# For fetching asset
import os

from noobish.core import type_switch
from ..location import location_custom_nodes
from ...common import string_extract_filename
from ...config import variables
from ...shell import shell_command


# Design to fetch an asset into comfyUI
def fetch_asset(value: dict):
    # Getting te asset type
    asset_type = value.get('type')
    asset_name = value.get('name')
    asset_url = value.get('location')
    root_dir = variables('root')
    comfy_dir = variables('name.comfy')

    # Go to the correct folder
    os.chdir(f"{root_dir}/{comfy_dir}/models/{asset_type}")

    # Setting the asset name as required
    if not asset_name is None:
        # Set it to asset name
        file_name = asset_name
    else:
        file_name = string_extract_filename(asset_url)

    # for loading files
    if not os.path.exists(file_name):
        shell_command(f'wget -O "{file_name}" "{asset_url}"')
    return


# For fetching lora assets
def fetch_asset_loras(name: str, location: str):
    fetch_asset({
        "type": "loras",
        "name": name,
        "location": location,
    })


def fetch_asset_checkpoints(name: str, location: str):
    fetch_asset({
        "type": "checkpoints",
        "name": name,
        "location": location,
    })


# Design for Fetching a Custom Node
def fetch_custom_node(value):
    # Need to work out what the value actually is first
    data = type_switch(value, {
        "str": lambda string: {
            "git": value,
        },
        # If it is dictionary. Assume it is exactly that
        "dict": lambda dictionary: dictionary
    })

    # Reading the Folder Name
    folder_name = string_extract_filename(data.get("git"))

    # Change to Custom Node Folder
    os.chdir(location_custom_nodes())

    # Remove whatever version it is
    shell_command(f"rm -rf {folder_name}")

    # Cloning from git
    shell_command(f"git clone {data.get('git')}")

    # Go into the folder
    os.chdir(f"{location_custom_nodes()}/{folder_name}")

    # Do we need checkout to a specific version?
    commit = data.get("commit")
    if not commit is None:
        # Checking out the commit
        shell_command(f"git checkout {commit}")

    # Install the requirement (if it exists)
    if os.path.exists("requirements.txt"):
        shell_command(f"{variables('pip')} install -r requirements.txt")
