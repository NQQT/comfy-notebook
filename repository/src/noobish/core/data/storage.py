from ..dict import dict_access
from ..type import type_switch


# For crea
def data_storage(store=None):
    # Building a new storage
    if store is None:
        store = {}

    # Building a handler function
    def accessor(data=None):
        nonlocal store

        return type_switch(data, {
            # if it is a string, then return the store value
            "str": lambda key: dict_access(store, key),
            # merging recursively
            "dict": lambda updated: dict_merge(store, updated),
            # By default, simply return the store data
            "default": lambda args: store
        })

    # Return the accessor to be used
    return accessor
