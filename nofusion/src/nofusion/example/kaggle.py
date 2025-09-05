# Starting Kaggle Example
def kaggle_start(root="/kaggle/working"):
    from nofusion.comfy import install_comfy_ui, start_pinggy_tunnel
    from nofusion.config import variables
    from nofusion.install import install_venv
    # Starting with Kaggle
    from nofusion.setup import setup_cyber_realistic

    # Setting the variables
    variables({
        # Require to define the correct root for kaggle
        "root": root
    })

    # Installing virtual env
    install_venv()
    install_comfy_ui()

    # Setting up Cyber realistic
    setup_cyber_realistic()

    # Just run CPU for now
    start_pinggy_tunnel()
