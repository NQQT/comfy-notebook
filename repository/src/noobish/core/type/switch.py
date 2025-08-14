from .name import type_name

# Standard type switch functionality
def type_switch(value, cases:dict):
    # Getting the callback
    callback = cases.get(type_name(value)) or cases.get("default")

    if callback is not None:
        # Triggering callback
        return callback({
            "value": value
        })

    # Return Nothing
    return None