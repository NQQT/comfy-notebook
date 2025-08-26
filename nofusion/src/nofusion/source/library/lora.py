from ..civitai import civitai_fetch_loras
from ...comfy import fetch_asset_loras


# For Installing Loras From Sources
def source_wan_i2v_lightning_loras():
    # The Location
    lora_location = "https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan22-Lightning"
    # Lightning Loras
    fetch_asset_loras(
        f"{lora_location}/Wan2.2-Lightning_I2V-A14B-4steps-lora_HIGH_fp16.safetensors")
    fetch_asset_loras(
        f"{lora_location}/Wan2.2-Lightning_I2V-A14B-4steps-lora_LOW_fp16.safetensors")


def source_wan_i2v_nsfw_loras():
    # Cock Play
    civitai_fetch_loras("CockPlay_i2v_HighNoise", "2087173")
    civitai_fetch_loras("CockPlay_i2v_LowNoise", "2087124")

    # General NSFW
    civitai_fetch_loras("GeneralNSFW_i2v_HighNoise", "2073605")
    civitai_fetch_loras("GeneralNSFW_i2v_LowNoise", "2083303")

    # Facial Cumshot
    civitai_fetch_loras("FacialShot_i2v_HighNoise", "2103700")
    civitai_fetch_loras("FacialShot_i2v_LowNoise", "2103699")

    # Deep Throat
    civitai_fetch_loras("DeepThroat_i2v_HighNoise", "2122049")
    civitai_fetch_loras("DeepThroat_i2v_LowNoise", "2124073")

    # Oral Insertion
    # civitai_fetch_loras("OralInsertion_i2v", "2121297")

    # Anime cumshot Aesthetics
    civitai_fetch_loras("AnimeCumshotAesthetics_i2v_HighNoise", "2116008")
    civitai_fetch_loras("AnimeCumshotAesthetics_i2v_LowNoise", "2116027")
