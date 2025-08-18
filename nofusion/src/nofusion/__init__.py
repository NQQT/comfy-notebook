def kaggle_start():
    from nofusion.comfy import install_comfy_ui, start_pinggy_tunnel
    from nofusion.config import variables
    from nofusion.install import install_venv
    # Starting with Kaggle
    from nofusion.setup import setup_cyber_realistic

    variables({
        # Require to define the correct root for kaggle
        "root": "/kaggle/working"
    })

    # Installing virtual env
    install_venv()
    install_comfy_ui()

    setup_cyber_realistic()

    # Just run CPU for now
    start_pinggy_tunnel("--cpu")
