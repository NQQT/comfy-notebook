# For Installing Models
from ...comfy import fetch_asset_diffusion_models, fetch_asset_text_encoders, fetch_asset_vae, fetch_asset_checkpoints


def source_model_wan_i2v_all_in_one():
    # Fetching Checkpoints
    fetch_asset_checkpoints(
        "https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne/resolve/main/v9/wan2.2-i2v-rapid-aio-nsfw-v9.2.safetensors")


# For installing wan image to video
# This is wan2.2
def source_model_wan_i2v(model_size="14B_Q8_0"):
    location_source = "https://huggingface.co/bullerwins/Wan2.2-I2V-A14B-GGUF/resolve/main"

    # Start Downloading
    fetch_asset_diffusion_models(f"{location_source}/wan2.2_i2v_high_noise_{model_size}.gguf")
    fetch_asset_diffusion_models(f"{location_source}/wan2.2_i2v_low_noise_{model_size}.gguf")

    # Required Text Encoder
    fetch_asset_text_encoders(
        "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors")

    # Required Vae
    fetch_asset_vae(
        "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors")
