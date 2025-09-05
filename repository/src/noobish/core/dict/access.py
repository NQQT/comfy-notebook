# For Accessing a dictionary value (even if it doesn't exist)
def dict_access(dictionary: dict, path: str):
    # This is the result key
    result = dictionary

    for key in path.split("."):
        # Updating result if it doesn't exist
        result[key] = result[key] or {}
        # Reassigning the pointer
        result = result[key]

    return result
