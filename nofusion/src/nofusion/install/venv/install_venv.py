import os
import stat

from nofusion.config import variables
from nofusion.shell import shell_command
from noobish.core import path_find_folders
from noobish.core.path.symbolic import path_symbolic_python3


# List of library to install
def install_libraries(pip):
    package_dir = os.path.dirname(__file__)
    # Setting up the minimum requirements
    minimum_requirement = os.path.join(package_dir, 'requirement', "minimum.txt")

    # Executing Shell Command
    shell_command(
        f"cd {variables('root')}",
        f"{pip} install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121",
        f"{pip} install tensorflow[and-cuda]",
        f"{pip} install -r {minimum_requirement}"
    )


# This is to install virtual env for python
def install_venv(data=variables):
    # Getting Python
    python = variables('python')

    # First. Run Virtual Env
    shell_command(f"{python} -m pip install virtualenv")

    venv_path = f'{data("root")}/venv'
    if not os.path.exists(venv_path):
        print('installing venv')

        # Change to the current environments
        os.chdir(data("root"))
        shell_command(f'cd {data("root")}')
        # Installing virtual env
        shell_command('virtualenv venv')

        # Installing library into venv
        install_libraries(f"{venv_path}/bin/python3 -m pip")
    else:
        # Scanning for the bin folders
        bin_folders = path_find_folders(venv_path, "bin")
        for bin_folder in bin_folders:
            # For each file within the bin folder
            for filename in os.listdir(bin_folder):
                # Create the file_path
                file_path = os.path.join(bin_folder, filename)
                # Checking that it is a file_path
                if os.path.isfile(file_path):
                    # Reconfiguring the permission
                    current_permissions = os.stat(file_path).st_mode
                    # Add execute permissions for the user, group, and others
                    os.chmod(file_path, current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    # Creating Symbolic Links, so that python and python3 points to venv environment
    # !ln -s {working_dir}/venv/bin/python3 {working_dir}/venv/bin/python
    python3_path = path_symbolic_python3()
    venv_path_python = f"{venv_path}/bin/{os.path.basename(python3_path)}"

    # Creating a Copy
    if not os.path.exists(venv_path_python):
        shell_command(f'cp {python3_path} {venv_path}/bin/')

    # Creating symbolic link
    shell_command(
        f"ln -s {venv_path_python} {venv_path}/bin/python",
        f"ln -s {venv_path_python} {venv_path}/bin/python3"
    )

    # Return the location of python3
    return f'{venv_path}/bin/python3'


# Only export the install one
__all__ = ["install_venv"]
