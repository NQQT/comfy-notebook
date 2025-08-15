from noobish.core import type_switch


# Define for shell execution
def shell_command(*commands):
    ipython = get_ipython()

    # ipython should exist
    if ipython is None:
        return

    # Processing each command
    for command in commands:
        # Base on command type. Execute as required
        type_switch(command, {
            # Executing the command
            "str": lambda args: ipython.system(args["value"])
        })
