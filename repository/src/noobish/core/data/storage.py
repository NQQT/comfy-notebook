from ..dict import dict_access, dict_update
from ..type import type_switch


# For crea
def data_storage(store=None):
    # Building a new storage
    if store is None:
        store = {}

    # Building a handler function
    def accessor(data=None):
        nonlocal store

        # Base on the type, different things will happen
        return type_switch(data, {
            # if it is a string, then return the store value
            "str": lambda args: dict_access(store, args['value']),
            # update dictionary
            "dict": lambda args: dict_update(store, args['value']),
            # By default, simply return the store data
            "default": lambda: store
        })

    # Return the accessor to be used
    return accessor
