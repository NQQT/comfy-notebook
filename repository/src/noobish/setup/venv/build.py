# This is to set up virtual environment for python3 on Kaggle (to save on import later)

import os
import sys
import stat

# For installing virtualenv
def setup_virtualenv(root_dir = os.getcwd(), python = sys.executable):
    try:
        ipython = get_ipython()
    except NameError:
        ipython = None

    if ipython is None:
        print("Ipython is not available.")
        return None

    # First, install virtualenv
    ipython.system(f"{python} -m pip install virtualenv")

    def find_bin_folders(folder_path):
        bin_folders = []
        for root, dirs, files in os.walk(folder_path):
            for dir_name in dirs:
                if dir_name == 'bin':
                    bin_folders.append(os.path.join(root, dir_name))
        return bin_folders

    def install_libraries(pip):
        nonlocal root_dir, ipython

        os.chdir(root_dir)

        ipython.system(f'{pip} install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121')
        ipython.system(f'{pip} install tensorflow[and-cuda]')
        # TODO: download req.txt
        ipython.system('wget https://q4j3.c11.e2-5.dev/downloads/req.txt')
        ipython.system(f'{pip} install -r {root_dir} / req.txt')

    if not os.path.exists(f'{root_dir}/venv'):
        print('installing venv')
        os.chdir(root_dir)
        ipython.system(f'cd {root_dir}')

        ipython.system('virtualenv venv')

        # Installing library into venv
        install_libraries(f"{root_dir}/venv/bin/python3 -m pip")
    else:
        bin_folders = find_bin_folders(f'{root_dir}/venv')
        if bin_folders:
          print("Found 'bin' folders:")
          for bin_folder in bin_folders:
            print(bin_folder)
            for filename in os.listdir(bin_folder):
                file_path = os.path.join(bin_folder, filename)
                if os.path.isfile(file_path):
                    current_permissions = os.stat(file_path).st_mode
                     # Add execute permissions for the user, group, and others
                    os.chmod(file_path, current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    # Return the location of python3
    return f'{root_dir}/venv/bin/python3'

    # Creating Symbolic Links, so that python and python3 points to venv environment
    # !ln -s {working_dir}/venv/bin/python3 {working_dir}/venv/bin/python