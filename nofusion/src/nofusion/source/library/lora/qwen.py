from ..model.qwen import source_model_qwen_edit
from ...civitai import civitai_fetch_loras


# Installing useful loras
def source_lora_qwen_edit_useful():
    # Need to loading standard qwen model first
    source_model_qwen_edit()
    
    # Anime to Realism: https://civitai.com/models/1934100
    civitai_fetch_loras("anime_2_realism", "2189067")
