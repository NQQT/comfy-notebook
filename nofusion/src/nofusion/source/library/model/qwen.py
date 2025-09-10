from nofusion.comfy import fetch_asset_diffusion_models


def source_model_qwen_edit(model_size="Q8_0"):
    location_source = "https://huggingface.co/QuantStack/Qwen-Image-Edit-GGUF/resolve/main"

    # Downloading Qwen Model
    fetch_asset_diffusion_models(f"{location_source}/Qwen_Image_Edit-{model_size}.gguf")
