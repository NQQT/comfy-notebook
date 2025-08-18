from ...config import variables
from ...shell import shell_command


# For installing packages
def install_package(*packages):
    # Setting packages
    for package in packages:
        # Install from Operation
        shell_command(f"{variables('pip')} install {package}")
