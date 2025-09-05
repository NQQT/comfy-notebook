import inspect

from .name import type_name


# Standard type switch functionality
def type_switch(value, cases: dict):
    # Getting the callback
    callback = cases.get(type_name(value)) or cases.get("default")

    # If callback is None. return none
    if callback is None:
        return None

    # Checking parameter. If it is 0, then return call with nothing
    if len(inspect.signature(callback).parameters) == 0:
        return callback()

    # Otherwise callback
    return callback({
        "value": value
    })
