import os
import subprocess


def path_symbolic_python3():
    # 1. Get the initial path as a string
    which_process = subprocess.run(
        ["which", "python3"],
        capture_output=True,
        text=True,
        check=True  # This will raise an exception if the command fails
    )

    # Return the python 3 Symbolic Path
    return path_symbolic_root(which_process.stdout.strip())


def path_symbolic_create(original_location: str, symbolic_location: str):
    # 1. Get the initial path as a string
    which_process = subprocess.run(
        ["which", "python3"],
        capture_output=True,
        text=True,
        check=True  # This will raise an exception if the command fails
    )
    return which_process.stdout.strip()


def path_symbolic_root(path: str):
    """
    Finds the ultimate target of a symbolic link path for the python executable
    using subprocess calls.
    """
    try:
        # 2. Loop until the path is no longer a symbolic link
        #    os.path.islink() is a much better way to check this.
        while os.path.islink(path):
            # 3. Correctly run "ls -l" and capture the output
            ls_process = subprocess.run(
                ["ls", "-l", path],
                capture_output=True,
                text=True,
                check=True
            )
            # 4. Parse the output to get the target of the link
            #    Example output: '... /usr/bin/python3 -> python3.10'
            output = ls_process.stdout.strip()
            new_path = output.split(' -> ')[1]

            # 5. If the linked path is relative, resolve it
            if not os.path.isabs(new_path):
                # Get the directory of the symlink itself
                link_dir = os.path.dirname(path)
                # Join it with the relative path to get the full path
                new_path = os.path.join(link_dir, new_path)

            path = new_path

        # Return the final, resolved path
        return path

    except (subprocess.CalledProcessError, FileNotFoundError, IndexError) as e:
        print(f"An error occurred: {e}")
        return None


__all__ = ["path_symbolic_root", "path_symbolic_create"]
