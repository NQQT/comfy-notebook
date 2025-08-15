import os
import re


# For finding folder within path
def path_find_folders(starting_path, regex_string=""):
    # Results
    results = []

    # Scanning through hfile
    for root, dirs, files in os.walk(starting_path):
        for dir_name in dirs:
            if re.match(regex_string, dir_name):
                results.append(os.path.join(root, dir_name))

    # Return results
    return results


# For finding files within path
def path_find_files(starting_path, regex_string):
    results = []
    # Scanning through hfile
    for root, dirs, files in os.walk(starting_path):
        for file_name in files:
            if re.match(regex_string, file_name):
                results.append(os.path.join(root, file_name))

    return results
