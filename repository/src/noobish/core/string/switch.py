# Use relative import to prevent circular issue
import inspect


def string_switch(value, cases: dict):
    # Getting the callback
    callback = cases.get(str(value)) or cases.get("default")

    if callback is not None:
        # Checking parameter. If it is 0, then return call with nothing
        if len(inspect.signature(callback).parameters) == 0:
            return callback()
        
        # Triggering callback
        return callback({
            "value": value
        })

    return None
