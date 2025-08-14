# Use relative import to prevent circular issue
from ..type.name import type_name

def string_switch(value,cases:dict):
    # Getting the callback
    callback = cases.get(str(value)) or cases.get("default")

    if callback is not None:
        # Triggering callback
        return callback({
            "value": value
        })

    return None