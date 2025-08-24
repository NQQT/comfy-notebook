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
