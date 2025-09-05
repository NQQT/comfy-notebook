import subprocess

from noobish.core import path_find_folders


def test():
    result = subprocess.run(["where", "python"])

    print(result)


def test_path_find_folders():
    # Get all possible folder
    result = path_find_folders("../")
    # There are more than 0 folders
    assert len(result) > 0

    # Can determine all the possible folders
    result = path_find_folders("../", "path")
    assert len(result) == 1
