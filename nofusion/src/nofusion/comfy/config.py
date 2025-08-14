# For configuring the variables
from nofusion.config import variables


def configure_variables():
    # Getting the root directory
    root_dir = variables("root")

    variables("dir")({
        "custom_nodes": ""
    })
