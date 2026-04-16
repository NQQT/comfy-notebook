from ....comfy import fetch_custom_node, fetch_asset_checkpoints, fetch_asset_loras, fetch_asset_latent_upscale_model, \
    fetch_asset_text_encoders


def source_model_ltx2():
    # Installing necessary ltx nodes
    fetch_custom_node("https://github.com/Lightricks/ComfyUI-LTXVideo")
    fetch_custom_node("https://github.com/evanspearman/ComfyMath")

    # Fetching checkpoints
    fetch_asset_checkpoints(
        "https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-22b-dev.safetensors");

    fetch_asset_loras(
        "https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-22b-distilled-lora-384.safetensors"
    )

    fetch_asset_latent_upscale_model(
        "https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-spatial-upscaler-x2-1.0.safetensors"
    )

    fetch_asset_text_encoders(
        "https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it.safetensors?download=true"
    )

    # Include these loras
    fetch_asset_loras(
        "https://huggingface.co/Sentinel7/ltxv/resolve/main/2378690/2674954/LTX2-i2v-SexThrust.safetensors")
    fetch_asset_loras(
        "https://huggingface.co/UnifiedHorusRA/028220/resolve/main/LTX2_-_Oral_Suite/LTXV/LTX2-i2v-OralSuite.safetensors",
        "LTX2-Oral-Suite.safetensors"
    )
    fetch_asset_loras(
        "https://huggingface.co/Sentinel7/ltxv/resolve/main/2352621/2668170/TittyvidLTX_000007750.safetensors",
        "LTX2-Better-Titty.safetensors"
    )
    fetch_asset_loras(
        "https://huggingface.co/matedivya/ponylora-jan27/resolve/main/102-Better-Female-Nudity-jan27.safetensors",
        "LTX2-Better-Female-Nudity.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/Sentinel7/ltxv/resolve/main/2332473/2729047/Penile_Praxis_V3.1.safetensors",
        "LTX2-Praxis-General.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/ThirdTimesTheCiarc/base_latex/resolve/main/2032489/2682194/manga_beret%20mix.safetensors",
        "LTX2-Manga-Style.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/Sentinel7/ltxv/resolve/main/2416244/2716592/LTXTF_000011500.safetensors",
        "LTX2-Titty-Fun.safetensors"
    )

    fetch_asset_loras(
        "https://huggingface.co/UnifiedHorusRA/028220v2/resolve/main/POV_NSFW_LTX2_Updated_v3_0/LTXV2/povnsfw-v3-complete.safetensors",
        "LTX2-General-Pov.safetensors"
    )

    # All in one: https://civitai.com/models/1811313/dr34ml4y-all-in-one-nsfw-wanltx2?modelVersionId=2747549
    fetch_asset_loras(
        "https://civitai.com/api/download/models/2747549?type=Model&format=SafeTensor&token=813701a486b32b80542dd5606dd8efdf",
        "LTX2-DR34ML4Y-AllInOne.safetensors"
    )