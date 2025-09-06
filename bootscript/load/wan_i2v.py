from nofusion.source import source_model_wan_i2v, source_wan_i2v_lightning_loras, \
    source_wan_i2v_nsfw_loras

# Running common file first
with open("../common.py") as file:
    exec(file.read())

# Only Q6 can fit right now
source_model_wan_i2v()
source_wan_i2v_lightning_loras()
source_wan_i2v_nsfw_loras()
