from ...civitai import civitai_fetch_loras


# Installing useful loras
def source_lora_qwen_edit_useful():
    # Anime to Realism: https://civitai.com/models/1934100
    civitai_fetch_loras("qwen_anime_2_realism", "2189067")

    # Outfit extractor: https://civitai.com/models/1940557?modelVersionId=2196307
    civitai_fetch_loras("qwen_outfit_extractor", "2196307")

    # Try on outfit: https://civitai.com/models/1940532?modelVersionId=2196278
    civitai_fetch_loras("qwen_try_on", "2196278")
