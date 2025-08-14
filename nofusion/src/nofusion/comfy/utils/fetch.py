# For fetching asset
import os
from urllib.parse import urlsplit

from nofusion.common import string_extract_filename
from nofusion.config import variables
from noobish.core import type_switch

# Design to fetch an asset into comfyUI
def fetch_asset(value):
    # Normalising Data
    data = type_switch(value,{
        "str":lambda string: {

        }
    })




def fetch_custom_node(value):
    # Need to work out what the value actually is first
    data = type_switch(value,{
        "str":lambda string: {
            "git": value
        },
        # If it is dictionary. Assume it is exactly that
        "dict": lambda dictionary: dictionary
    })

    # Reading the Folder Name
    folder_name = string_extract_filename(data["git"])

    %cd {working_dir}/ComfyUI/custom_nodes
    # Remove whatever version it is
    !rm -rf {folder_name}
    !git clone {git_url}

    # Go into the folder
    %cd {variables("folder_custom_nodes")}/{folder_name}


    # Do we need checkout to a specific version?
    if not commit is None:
        !git checkout {commit}

    # Install the requirement (if it exists)
    if os.path.exists("requirements.txt"):
        !{variables("pip")} install -r requirements.txt

    # Return to the working directory
    %cd {working_dir}

    # Clearing the output to show python has been updated
    # clear_output()




