import os

from noobish.core import type_switch


# Define for shell execution
def shell_command(*commands):
    # Processing each command
    for command in commands:
        # Base on command type. Execute as required
        type_switch(command, {
            # Executing the command
            "str": lambda args: os.system(args["value"])
        })
