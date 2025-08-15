from ..check import is_dict


# For updating a dictionary by reference
def dict_update(original: dict, update: dict):
    # Scanning through the item listing
    for key, value in update.items():
        # Checking if value of first dict is a dictionary and second is a dictionary
        if key in original and is_dict(original[key]) and is_dict(value):
            # Recursive merging
            dict_update(original[key], value)
        else:
            original[key] = value

    # returning the dictionary
    return original
