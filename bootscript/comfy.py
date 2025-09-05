import os

# Git Repo Name
git_repo_name = "comfy-notebook"

os.system(f"pip install --upgrade {git_repo_name}/repository")
os.system(f"pip install --upgrade {git_repo_name}/nofusion")

from nofusion.comfy import install_comfy_ui
from nofusion.config import variables

variables({
    # Setting OS
    "root": os.getcwd()
})

# Installing ComfyUI
install_comfy_ui()
