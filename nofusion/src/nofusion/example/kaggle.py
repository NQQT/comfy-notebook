from nofusion.comfy import initiate_comfy_ui_thread, start_comfy_ui_slave, log_setup
from nofusion.config import variables

# Configuring Variables
configure_variables()

# Global variable configuration
variables({
    # The name of this agent
    "name": {
        "agent": "james"
    },
    "stash": "kaggle_test",
    # Define the cloud environment for optimisation
    "cloud": "kaggle",
    # Use Coda Version 118
    "cuda": "118",
    # Require to define the correct root for kaggle
    "root": "/kaggle/working"
})

# Setting up comfy server
log_setup("comfy-server")
initiate_comfy_ui_thread()

# Starting the slave
log_setup("initialising")
start_comfy_ui_slave()
