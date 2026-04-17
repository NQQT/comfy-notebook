import os
import warnings

from ..comfy import fetch_asset
from ..config import variables
from ..shell import shell_command

warnings.filterwarnings("ignore")
from huggingface_hub import login
# or login() for interactive widget
from huggingface_hub import HfApi


# This is for copying a file into hugging face
def huggingface_mirror(token: str, location: str, path_in_repo, repo_id: str):
    # Returns back to root
    shell_command(f'cd {variables("root")}')

    # Temporary name
    filename = "TemporaryFile.safetensors"

    # Fetching the required asset
    fetch_asset({
        "type": "temporary",
        "name": filename,
        "location": location,
    })

    # What temporary file path this should be?
    filepath = f"{variables("root")}/ComfyUI/models/temporary/{filename}"

    # Uploading to Huggingface
    login(token)
    api = HfApi()
    api.upload_file(
        path_or_fileobj=filepath,
        path_in_repo=path_in_repo,
        repo_id=repo_id,
        repo_type="model",
    )

    # Delete the file
    os.remove(filepath)
