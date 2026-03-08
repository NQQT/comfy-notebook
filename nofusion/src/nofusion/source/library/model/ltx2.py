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
