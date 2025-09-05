from ..check import is_dict


# for merging a two dictionary together
def dict_merge(first_dict: dict, second_dict: dict):
    # The result to be returned
    result = {**first_dict}

    # Scanning through the item listing
    for key, value in second_dict.items():
        # Checking if value of first dict is a dictionary and second is a dictionary
        if key in result and is_dict(result[key]) and is_dict(value):
            # Recursive merging
            result[key] = dict_merge(result[key], value)
        else:
            result[key] = value

    # returning the dictionary
    return result
