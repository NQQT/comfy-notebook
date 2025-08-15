from noobish.core.data import data_storage

# Defining the data storage variable
variables = data_storage({
    # Default pip, should just be pip
    "pip": "pip",
    # Default python should just be python for now
    "python": "python",
    # The root directory is whatever the current directory is
    "root": "./",
    # Initial Data Configuration
    "name": "ComfyUI"
})
