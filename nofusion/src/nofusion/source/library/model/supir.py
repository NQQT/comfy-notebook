from nofusion.comfy import fetch_asset_checkpoints


# Installing Supir Upscaler
def source_model_supir_upscale():
    # Require SUPIR v0Q
    fetch_asset_checkpoints("https://huggingface.co/Kijai/SUPIR_pruned/resolve/main/SUPIR-v0Q_fp16.safetensors")
