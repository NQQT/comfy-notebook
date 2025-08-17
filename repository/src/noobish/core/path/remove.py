from nofusion.shell import shell_command


# For removing a path. Usually mean deleting
def path_remove(*paths):
    # Processing each command
    for path in paths:
        # Removing all files within path
        shell_command(f"rm -rf {path}")
