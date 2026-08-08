import os

from .config import configure_variables
from .location import location_ipadaptor
from .utils import fetch_custom_node
from ..config import variables
from ..install import install_package
from ..shell import shell_command


# For Reinstalling Comfy UI (if something went wrong)
def reinstall_comfy_ui(checkout_version=None):
    # Getting the variables
    root_dir = variables("root")
    comfy_name = variables("name.comfy")
    os.chdir(root_dir)

    # Remove ComfyUI Completely
    shell_command(f"rm -rf ${comfy_name}")

    # Installing ComfyUI
    install_comfy_ui(checkout_version)


# For installing comfy UI
def install_comfy_ui(checkout_version=None):
    # Configuring Variables
    configure_variables()

    # Getting the variables
    root_dir = variables("root")
    comfy_name = variables("name.comfy")

    os.chdir(root_dir)
    # Executing Shell Commands
    # Cloning Comfy UI

    shell_command(f"git clone https://github.com/comfyanonymous/ComfyUI.git {comfy_name}")

    os.chdir(f"{root_dir}/{comfy_name}")

    # Checking out a branch
    if not checkout_version is None:
        shell_command(f"git checkout {checkout_version}")

    pip = variables("pip")

    # Installing the necessary requirements
    shell_command(f"{pip} install -r requirements.txt")

    # Creating Temporary Folder
    shell_command(
        # Require the ip-adapter Folder
        f"mkdir {location_ipadaptor()}"
    )

    # Additional installation to use
    install_package(
        "pillow",
        "insightface",
        "onnxruntime",
        "onnxruntime-gpu",
        "matplotlib-inline",
    )

    # SageAttention 2.2.0 (provides SageAttention2++ kernels) is NOT published
    # on PyPI — https://pypi.org/pypi/sageattention/json shows the latest
    # published release is 1.0.6 (2024-11-20), which is the old Triton-only
    # v1 branch. 2.x must be installed from the GitHub repo at tag v2.2.0
    # (commit eb615cf6cf4d221338033340ee2de1c37fbdba4a).
    #
    # --no-build-isolation is MANDATORY: v2.2.0's setup.py imports torch
    # (torch.utils.cpp_extension.CUDAExtension) at module level to compile
    # csrc/qattn CUDA kernels, but its pyproject.toml only declares
    # setuptools/wheel/packaging as build requirements — an isolated pip
    # build env would fail on `import torch`. Because isolation is off, pip
    # also does NOT auto-provision those build requirements, so they are
    # installed explicitly first (versions mirror pyproject.toml).
    #
    # Build prerequisites that must exist in the environment BEFORE this runs:
    #   - torch already installed (modal_comfy_rtx6000.py installs the cu132
    #     wheels in setup_comfy() BEFORE calling install_comfy_ui)
    #   - nvcc (CUDA toolkit >= 12.8 for sm_120/Blackwell) at $CUDA_HOME/bin/nvcc
    #   - TORCH_CUDA_ARCH_LIST set (setup.py aborts with "No target compute
    #     capabilities" when it cannot probe a GPU, e.g. GPU-less image builds)
    #   - a C++ toolchain + libgomp (CXX_FLAGS use -fopenmp -lgomp)
    shell_command(
        f'{pip} install "setuptools>=62,<75" "wheel>=0.38,<0.44" "packaging>=21,<24" ninja'
    )
    shell_command(
        f"{pip} install --no-build-isolation "
        "git+https://github.com/thu-ml/SageAttention.git@v2.2.0"
    )

    # For installing custom nodes
    # Download Comfy UI Manager
    # fetch_custom_node("https://github.com/Comfy-Org/ComfyUI-Manager")

    fetch_custom_node("https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite")
    fetch_custom_node("https://github.com/kijai/ComfyUI-KJNodes")
    # git_custom_node("https://github.com/yolain/ComfyUI-Easy-Use","717092a3ceb51c474b5b3f77fc188979f0db9d67")
    fetch_custom_node("https://github.com/rgthree/rgthree-comfy")
    # RES_2S Sampler (better and sharper)
    fetch_custom_node("https://github.com/ClownsharkBatwing/RES4LYF")
    # for loading GGUF model
    fetch_custom_node("https://github.com/city96/ComfyUI-GGUF")
    # For interpolation, but LTX23 is better now days.
    # fetch_custom_node("https://github.com/kijai/ComfyUI-GIMM-VFI")
    # For running Cloud Based ComfyUI with Local Controls
    fetch_custom_node("https://github.com/comfyscript/ComfyUI-CloudClient")
    # For Upscaling and So on
    # fetch_custom_node("https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler")
    # For Upscaling and so on
    fetch_custom_node("https://github.com/Comfy-Org/Nvidia_RTX_Nodes_ComfyUI")
    # Sol Attention
    fetch_custom_node("https://github.com/Saganaki22/ComfyUI-sol-attn")

    # Krea2 Custom Nodes
    fetch_custom_node("https://github.com/lbouaraba/comfyui-krea2edit")

    # Cleaning and Purging
    fetch_custom_node("https://github.com/chflame163/ComfyUI_LayerStyle")
    fetch_custom_node("https://github.com/LAOGOU-666/Comfyui-Memory_Cleanup")

    # Spectrum
    fetch_custom_node("https://github.com/benjiyaya/ComfyUI-Spectrum")

    # For minimax H3
    fetch_custom_node("https://github.com/Larryvrh/ComfyUI-MiniMax-H3-Turbo")