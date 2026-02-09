from nofusion.comfy import fetch_asset


# For loading SeedVR2 Upscaler
def source_model_seedvr2_upscale():
    # Fetching the required model
    fetch_asset({
        # Specifically Save to Models/SEEDVR2 Spot
        "type": "models/SEEDVR2",
        "name": "seedvr2_ema_7b_fp16.safetensors",
        "location": "https://huggingface.co/numz/SeedVR2_comfyUI/resolve/main/seedvr2_ema_7b_fp16.safetensors?download=true",
    })
