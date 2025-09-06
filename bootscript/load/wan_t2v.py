from nofusion.source import source_model_wan_t2v, source_wan_t2v_lightning_loras, source_wan_t2v_nsfw_loras

# Running common file first
with open("../common.py") as file:
    exec(file.read())

# Loading T2V Model
source_model_wan_t2v()
source_wan_t2v_lightning_loras()
source_wan_t2v_nsfw_loras()
