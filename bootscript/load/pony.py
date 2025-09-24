import os

from nofusion.source import source_model_pony_cyber_realistic, civitai_fetch_loras, civitai_fetch_checkpoints

# Standard Comfy File Setup
package_dir = os.path.dirname(__file__)
# Setting up the minimum requirements
common_script = os.path.join(package_dir, '../common.py')
# Running common file first
with open(common_script, "r") as file:
    exec(file.read())

# Setting up Cyber realistic
source_model_pony_cyber_realistic()

# https://civitai.com/models/1559047?modelVersionId=1971591
civitai_fetch_checkpoints("LucentXLPonyByKlaabu", "1971591")

# https://civitai.com/models/1115064/pony-realism-slider?modelVersionId=1253021
civitai_fetch_loras("pony_realism", "1253021")

civitai_fetch_loras("pony_beauty_slider", "518458")
# https://civitai.com/models/341353/expressiveh-hentai-lora-style
civitai_fetch_loras("pony_expressive_h", "382152")
# https://civitai.com/models/553414?modelVersionId=615876
civitai_fetch_loras("pony_char_yoo_iseol", "615876")

#
civitai_fetch_loras("pony_char_seo_baek_hyang", "697834")
