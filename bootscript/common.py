import os

from nofusion.config import variables

# Setting up the variables
variables({
    # Setting OS
    "root": os.getcwd(),
    # Keys to be used for downloading
    "secret": {
        "civitai": "813701a486b32b80542dd5606dd8efdf"
    }
})
