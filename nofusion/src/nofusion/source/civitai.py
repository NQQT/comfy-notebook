# For generating a model link to download
from ..comfy import fetch_asset_checkpoints, fetch_asset_loras
from ..config import variables


def civitai_fetch_url(model_id, model_format="SafeTensor"):
    # Getting out the token
    token = variables("secret.civitai")

    # Downloading Civitai
    return f"https://civitai.com/api/download/models/{model_id}?type=Model&format={model_format}&fp=fp16&token={token}"


# For fetching civitai asset
def civitai_fetch_loras(model_name: str, model_id: str, ext="safetensors"):
    # Constructing the Lora URL
    model_url = civitai_fetch_url(model_id)
    # Fetching the asset checkpoints
    fetch_asset_loras(model_url, model_name + "." + ext)


# For fetching civitai asset
def civitai_fetch_checkpoints(model_name: str, model_id: str):
    # Constructing the Lora URL
    model_url = civitai_fetch_url(model_id)
    # Fetching the asset checkpoints
    fetch_asset_checkpoints(model_url, model_name + ".safetensors")
