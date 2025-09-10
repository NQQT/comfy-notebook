from nofusion.comfy import fetch_asset_diffusion_models, fetch_asset_text_encoders, fetch_asset_vae
from noobish.core import string_switch


# For installing Qwen Edit
def source_model_qwen_edit(model_size="Q8_0"):
    model_source = "https://huggingface.co/QuantStack/Qwen-Image-Edit-GGUF/resolve/main"
    encoder_source = "https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders"
    vae_source = "https://huggingface.co/QuantStack/Qwen-Image-GGUF/resolve/main/VAE/"

    # Downloading Qwen Model
    fetch_asset_diffusion_models(f"{model_source}/Qwen_Image_Edit-{model_size}.gguf")

    encoder_size = string_switch(model_size, {
        # if Q8_0, using high text-encoder is okay
        "Q8_0": lambda: "",
        # Everything should use scaled
        "default": lambda: "_fp8_scaled"
    })

    fetch_asset_text_encoders(f"{encoder_source}/qwen_2.5_vl_7b{encoder_size}.safetensors")

    # Vae
    fetch_asset_vae(f"{vae_source}/Qwen_Image-VAE.safetensors")
