# For generating a model link to download
from noobish.core import string_switch

from ..comfy import fetch_asset_checkpoints, fetch_asset_loras
from ..config import variables


def civitai_fetch_url(model_id, model_format="SafeTensor"):
    # Getting out the token
    token = variables("secret.civitai")

    # Downloading Civitai
    return f"https://civitai.com/api/download/models/{model_id}?type=Model&format={model_format}&fp=fp16&token={token}"


# For fetching civitai asset
def civitai_fetch_loras(model_name: str, model_id: str, ext="safetensors"):
    # This is for zip file
    def download_and_extract():
        # Constructing the Lora URL. Diffusers is for zip
        model_url = civitai_fetch_url(model_id, "Diffusers")
        file_downloaded = fetch_asset_loras(model_url, model_name + "." + ext)
        # Attempting to unpack
        import zipfile, os
        with zipfile.ZipFile(file_downloaded, "r") as zip_ref:
            zip_ref.extractall(os.path.dirname(file_downloaded))

        # Clearing it to prevent future download
        with open(file_downloaded, "r+") as file:
            file.seek(0)
            file.truncate()

    def standard_loras():
        # Constructing the Lora URL
        model_url = civitai_fetch_url(model_id)
        # Fetching the asset checkpoints
        return fetch_asset_loras(model_url, model_name + "." + ext)

    string_switch(ext, {
        # If it is zip files. Download it and start extraction
        "zip": download_and_extract,
        "default": standard_loras
    })


# For fetching civitai asset
def civitai_fetch_checkpoints(model_name: str, model_id: str):
    # Constructing the Lora URL
    model_url = civitai_fetch_url(model_id)
    # Fetching the asset checkpoints
    fetch_asset_checkpoints(model_url, model_name + ".safetensors")
