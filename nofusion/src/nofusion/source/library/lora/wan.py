from ...civitai import civitai_fetch_loras
from ....comfy import fetch_asset_loras


# For Installing Loras From Sources
def source_wan_i2v_lightning_loras():
    # The Location
    lora_location = "https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan22-Lightning"
    # Lightning Loras
    fetch_asset_loras(
        f"{lora_location}/Wan2.2-Lightning_I2V-A14B-4steps-lora_HIGH_fp16.safetensors")
    fetch_asset_loras(
        f"{lora_location}/Wan2.2-Lightning_I2V-A14B-4steps-lora_LOW_fp16.safetensors")


def source_wan_t2v_nsfw_loras():
    # Doggy Style
    civitai_fetch_loras("DoggyStyle_t2v_HighNoise", "2076026")
    civitai_fetch_loras("DoggyStyle_t2v_LowNoise", "2076035")

    # Facial Cumshot
    # https://civitai.com/models/1858645/facial-cumshot-t2v-wan-22-video-lora-k3nk
    # civitai_fetch_loras("FacialShot_t2v_HighNoise", "2103700")
    # civitai_fetch_loras("FacialShot_t2v_LowNoise", "2103699")


def source_wan_i2v_nsfw_loras():
    # Cock Play
    civitai_fetch_loras("CockPlay_i2v_HighNoise", "2087173")
    civitai_fetch_loras("CockPlay_i2v_LowNoise", "2087124")

    # General NSFW
    civitai_fetch_loras("GeneralNSFW_i2v_HighNoise", "2073605")
    civitai_fetch_loras("GeneralNSFW_i2v_LowNoise", "2083303")

    # Deep Throat
    civitai_fetch_loras("DeepThroat_i2v_HighNoise", "2122049")
    civitai_fetch_loras("DeepThroat_i2v_LowNoise", "2124073")

    # Blowjob
    # https://civitai.com/models/1497390/deepthroat-blowjob-wan-2x-i2v
    civitai_fetch_loras("Blowjob_i2v_HighNoise", "2152516")
    civitai_fetch_loras("Blowjob_i2v_LowNoise", "2152583")

    # Missionary
    civitai_fetch_loras("Missionary_i2v_HighNoise", "2098405")
    civitai_fetch_loras("Missionary_i2v_LowNoise", "2098396")

    # Assertive Cowgirl
    civitai_fetch_loras("AssertiveCowgirl_i2v_HighNoise", "2129122")
    civitai_fetch_loras("AssertiveCowgirl_i2v_LowNoise", "2129201")

    # https://civitai.com/models/1874153?modelVersionId=2121297
    civitai_fetch_loras("OInsertion_i2v", "2121297", "diffusers")
    # https://civitai.com/models/1905168/cumshot-wan-22
    civitai_fetch_loras("Cumshot_i2v", "2156421", "diffusers")
    # https://civitai.com/models/1923528/sex-fov-slider-wan-22
    civitai_fetch_loras("NSFWFOVSlider_i2v", "2177091", "diffusers")

    # Anime cumshot Aesthetics
    # https://civitai.com/models/1869475
    civitai_fetch_loras("AnimeCumshotAesthetics_i2v_HighNoise", "2116008")
    civitai_fetch_loras("AnimeCumshotAesthetics_i2v_LowNoise", "2116027")
