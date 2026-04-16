from ...civitai import civitai_fetch_loras
from ....comfy import fetch_asset_loras


# Installing useful loras
def source_lora_qwen_edit_useful():
    # Anime to Realism: https://civitai.com/models/1934100
    civitai_fetch_loras("qwen_anime_2_realism", "2189067")

    # Outfit extractor: https://civitai.com/models/1940557?modelVersionId=2196307
    civitai_fetch_loras("qwen_outfit_extractor", "2196307")

    # Try on outfit: https://civitai.com/models/1940532?modelVersionId=2196278
    civitai_fetch_loras("qwen_try_on", "2196278")

    # Lightning Loras
    fetch_asset_loras(
        "https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V2.0.safetensors")
    # fetch_asset_loras(
    #    "https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-8steps-V1.1.safetensors")
