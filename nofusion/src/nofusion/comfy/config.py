# For configuring the variables
from nofusion.config import variables


# For configuring the variables
def configure_variables():
    # Getting the root directory
    root_dir = variables("root")
    comfy_dir = variables("name.comfy")
    working_dir = f"{root_dir}/{comfy_dir}"

    # Updating all the directory path
    variables({
        # Directory Listing
        "dir": {
            "comfy": working_dir,
            # Location of the model
            "models": f"{working_dir}/models",
            # These are all comfy directory
            "custom_nodes": f"{working_dir}/custom_nodes",
        }
    })
