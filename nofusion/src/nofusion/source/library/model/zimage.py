# For Setting up Cyber Realistic
from ....comfy import fetch_asset_vae, fetch_asset_text_encoders
from ....source import civitai_fetch_diffusion_models


def source_model_zimage_moody_mix():
    # Moody Mix
    civitai_fetch_diffusion_models("ZImageMoodyMix", "2633363")

    # Text-encoder
    fetch_asset_text_encoders(
        "https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors")

    # AE
    fetch_asset_vae("https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors")
