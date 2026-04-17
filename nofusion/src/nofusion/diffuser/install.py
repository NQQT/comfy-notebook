from nofusion.comfy import configure_variables, shell_command
from nofusion.config import variables

# Configuring Variables
configure_variables()
pip = variables("pip")
shell_command(f"{pip} install diffusers transformers accelerate sentencepiece protobuf")
