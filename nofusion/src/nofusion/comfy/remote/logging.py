from noobish.web import Database

from ..config import variables


# Logging
def _log(status: str, details: str):
    # Accessing the cloud database
    stash_id = variables("stash");
    name = variables("name.agent");

    # Accessing database
    database = Database(f"{stash_id}_agent")

    # Pushing the item into the log
    database.push(f"{name}_{status}_{details}.status", {})


# Log idle state
def log_idle(details: str = ""):
    _log("idle", details)


# Log idle state
def log_busy(details: str = ""):
    _log("busy", details)


# Log idle state
def log_setup(details: str = ""):
    _log("setup", details)
