import os

# Setting up ComfyUI on a brand-new server
# Returning to Working Directory
git_repo_name = "comfy-notebook"

# Remove the repo
os.system(f"rm -rf {git_repo_name}")
# Running Comfy Setup
os.system(f"git clone --branch feature/venv-upgrade https://github.com/NQQT/{git_repo_name}.git")

os.system(f"pip install --break-system-packages --upgrade {git_repo_name}/repository")
os.system(f"pip install --break-system-packages --upgrade {git_repo_name}/nofusion")
