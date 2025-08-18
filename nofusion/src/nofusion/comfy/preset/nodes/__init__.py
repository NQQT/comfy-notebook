import os

from noobish.core import path_symbolic_create
from ....config import variables
from ....shell import shell_command


def nodes_symbolic_import():
    package_dir = os.path.dirname(__file__)
    # Getting the list of nodes within the folder
    node_list = [f for f in os.listdir(package_dir) if os.path.isdir(os.path.join(package_dir, f))]

    # Scanning through the folder
    for node_folder in node_list:
        custom_nodes_dir = f"{variables('root')}/{variables('name.comfy')}/custom_nodes/{node_folder}"
        # Remove a folder completely
        shell_command(f"rm -rf {custom_nodes_dir}")

        # Creating symbolic link
        path_symbolic_create(f"{package_dir}/{node_folder}", custom_nodes_dir)
