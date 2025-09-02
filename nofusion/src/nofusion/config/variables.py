import os

from noobish.core.data import data_storage

# Defining the data storage variable
variables = data_storage({
    # Default pip, should just be pip
    "pip": "pip",
    # Default python should just be python for now
    "python": "python",
    # The root directory is whatever the current directory is when first pull
    "root": os.getcwd(),
    # Initial Data Configuration
    "name": {
        "comfy": "ComfyUI",
    },
    # Storing Secrets
    "secret": {
        # Update your Key Listing Here
    }
})
