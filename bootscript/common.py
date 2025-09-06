import os

from nofusion.comfy import configure_variables
from nofusion.config import variables

# Setting up the variables
variables({
    # Setting OS
    "root": os.getcwd(),
    # Keys to be used for downloading
    "secret": {
        "civitai": "813701a486b32b80542dd5606dd8efdf"
    },
    "dir": {
        "models": ""
    }
})

# Configuring Standard Comfy Variables
configure_variables()
