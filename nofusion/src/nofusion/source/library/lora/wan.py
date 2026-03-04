from ...civitai import civitai_fetch_loras
from ....comfy import fetch_asset_loras


# For Installing Loras From Sources
def source_wan_i2v_lightning_loras():
    # The Location
    lora_location = "https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan22-Lightning"
    # Lightning Loras
    # fetch_asset_loras(f"{lora_location}/Wan2.2-Lightning_I2V-A14B-4steps-lora_HIGH_fp16.safetensors")
    # fetch_asset_loras(f"{lora_location}/Wan2.2-Lightning_I2V-A14B-4steps-lora_LOW_fp16.safetensors")

    lora_location = "https://huggingface.co/lightx2v/Wan2.2-Lightning/resolve/main/Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1"
    fetch_asset_loras(f"{lora_location}/high_noise_model.safetensors?download=true", "4step-lora-seko-high.safetensors")
    fetch_asset_loras(f"{lora_location}/low_noise_model.safetensors?download=true", "4step-lora-seko-low.safetensors")


def source_wan_i2v_nsfw_loras():
    # Dream play, All in one
    fetch_asset_loras(
        "https://huggingface.co/profpeng/nsfwv2/resolve/main/DR34ML4Y_I2V_14B_LOW_V2.safetensors",
        "DR34ML4Y_I2V_14B_LOW.safetensors"
    )
    fetch_asset_loras(
        "https://huggingface.co/profpeng/nsfwv2/resolve/main/DR34ML4Y_I2V_14B_HIGH_V2.safetensors",
        "DR34ML4Y_I2V_14B_HIGH.safetensors"
    )

    # Fetching all assets from iGoon because he's awesome!
    # https://civitaiarchive.com/users/iGoonHard
    fetch_asset_loras(
        "https://huggingface.co/SRodge00/blinkdoggy/resolve/main/iGoon%20-%20Blink_Front_Doggystyle_I2V_HIGH.safetensors",
        "iGoon_Blink_Front_DoggyStyle_I2V_HIGH.safetensors")
    fetch_asset_loras(
        "https://huggingface.co/SRodge00/blinkdoggy/resolve/main/iGoon%20-%20Blink_Front_Doggystyle_I2V_LOW.safetensors",
        "iGoon_Blink_Front_DoggyStyle_I2V_LOW.safetensors"
    )

    # Squatting: https://civitaiarchive.com/models/2203090?modelVersionId=2480524
    fetch_asset_loras(
        "https://huggingface.co/SRodge00/blinksquat/resolve/main/Blink_Squatting_Cowgirl_Position_I2V_HIGH.safetensors",
        "iGoon_Blink_SquattingCowgirl_I2V_HIGH.safetensors"
    )
    fetch_asset_loras(
        "https://huggingface.co/SRodge00/blinksquat/resolve/main/Blink_Squatting_Cowgirl_Position_I2V_LOW.safetensors",
        "iGoon_Blink_SquattingCowgirl_I2V_LOW.safetensors"
    )

    # Handjob
    fetch_asset_loras(
        "https://huggingface.co/SRodge00/hjblink/resolve/main/iGoon%20-%20Blink_Handjob_I2V_HIGH.safetensors",
        "iGoon_Blink_Handjob_I2V_HIGH.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/SRodge00/hjblink/resolve/main/iGoon%20-%20Blink_Handjob_I2V_LOW.safetensors",
        "iGoon_Blink_Handjob_I2V_LOW.safetensors"
    )

    # https://civitaiarchive.com/models/2172672?modelVersionId=2446684
    fetch_asset_loras(
        "https://huggingface.co/SRodge00/blinkbj/resolve/main/iGOON_Blink_Blowjob_I2V_HIGH(1).safetensors",
        "iGoon_Blink_BlowJob_I2V_HIGH.safetensors")

    fetch_asset_loras(
        "https://huggingface.co/SRodge00/blinkbj/resolve/main/iGOON_Blink_Blowjob_I2V_LOW(1).safetensors",
        "iGoon_Blink_BlowJob_I2V_LOW.safetensors")

    # Facial
    fetch_asset_loras(
        "https://huggingface.co/SRodge00/facialblink/resolve/main/iGoon%20-%20Blink_Facial_I2V_LOW.safetensors",
        "iGoon_Blink_Facial_I2V_LOW.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/SRodge00/facialblink/resolve/main/iGoon%20-%20Blink_Facial_I2V_HIGH.safetensors",
        "iGoon_Blink_Facial_I2V_HIGH.safetensors"
    )

    # Missionary
    fetch_asset_loras(
        "https://huggingface.co/SRodge00/blinkmissionary2/resolve/main/iGoon%20-%20Blink_Missionary_I2V_LOW%20v2.safetensors",
        "iGoon_Blink_Missionary_I2V_LOW.safetensors"
    )
    fetch_asset_loras(
        "https://huggingface.co/SRodge00/blinkmissionary2/resolve/main/iGoon_Blink_Missionary_I2V_HIGH%20v2.safetensors",
        "iGoon_Blink_Missionary_I2V_HIGH.safetensors"
    )

    # Boobjob
    fetch_asset_loras(
        "https://huggingface.co/baka-ending19/Wan2.2/resolve/main/iGoon_Blink_Titjob_I2V_HIGH.safetensors",
        "iGoon_Blink_Boobjob_I2V_HIGH.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/SR47/blinktitjob/resolve/main/iGoon_Blink_Titjob_I2V_LOW.safetensors",
        "iGoon_Blink_Boobjob_I2V_LOW.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/SRodge00/blinkbackdog/resolve/main/iGoon%20-%20Blink_Back_Doggystyle_HIGH.safetensors",
        "iGoon_Blink_Back_DoggyStyle_I2V_High.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/SRodge00/blinkbackdog/resolve/main/iGoon%20-%20Blink_Back_Doggystyle_LOW.safetensors",
        "iGoon_Blink_Back_DoggyStyle_I2V_Low.safetensors"
    )

    # Deepthroat / Facefuck Loras
    fetch_asset_loras(
        "https://huggingface.co/profpeng/deepthroat/resolve/main/Wan22_ThroatV3_High.safetensors",
        "CivitaiWolf_Deepthroat_v3_HIGH.safetensors"
    )
    fetch_asset_loras(
        "https://huggingface.co/Paolo222/DPaint/resolve/main/Wan22_Face_fuck_ThroatV3_Low.safetensors",
        "CivitaiWolf_Deepthroat_v3_LOW.safetensors"
    )

    # Cumshot / Facials
    fetch_asset_loras(
        "https://huggingface.co/jortestingss/facec/resolve/main/Wan22_CumV2_High.safetensors",
        "CivitaiWolf_Facial_v2_HIGH.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/Zachimo/WanCum2/resolve/main/Wan22_CumV2_Low.safetensors",
        "CivitaiWolf_Facial_v2_LOW.safetensors"
    )

    # Oral Creampie
    fetch_asset_loras(
        "https://huggingface.co/fiojanea/Esan_testi/resolve/main/wan22-mouthfull-140epoc-high-k3nk.safetensors",
        "K3NK_Mouthful_v1_HIGH.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/hank87/pnsenterfillmouthwn22/resolve/main/wan22-mouthfull-152epoc-low-k3nk.safetensors",
        "K3NK_Mouthful_v1_LOW.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/neph1/hard_cut_wan_lora/resolve/main/hard_cut_3_wan_i2v_high.safetensors",
        "Neph1_CinematicHardCut_v3_HIGH.safetensors"
    )


# This is considered old now.
def source_wan_i2v_nsfw_loras_old():
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
