import logging.config
import time
from pathlib import Path

import rootpath

PROJECT_DIRS = {
    "LOGS_DIR": "./logs",
}

rootpath.append()

t = int(time.time())
id = f'/{"_".join([str(t)])}'
id = ""


def filepath_as_log_id(path: str) -> str:
    """
    Generates a log_id from the path

    Added as "__main__" was not helpful in large logs. Passing __file__ into
    this function will normlise it from "./myscript.py" to "myscript". Easier to
    read in output logs and saves a bytes in output
    """
    if not path:
        return
    return str(
        Path(path).resolve().relative_to(rootpath.detect()).with_suffix("")
    ).replace("/", ".")


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
        },
        "extended": {
            "format": "%(asctime)s : %(levelname)s : [%(name)s] %(funcName)s: %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "extended",
            "level": "ERROR",
            "stream": "ext://sys.stdout",
        },
        "debug_file_handler": {
            "class": "logging.FileHandler",
            "formatter": "extended",
            "level": "DEBUG",
            "filename": str(f"{PROJECT_DIRS.get('LOGS_DIR')}/debug{id}.log"),
            "mode": "a",
        },
        "error_file_handler": {
            "class": "logging.FileHandler",
            "formatter": "extended",
            "level": "ERROR",
            "filename": str(f"{PROJECT_DIRS.get('LOGS_DIR')}/error{id}.log"),
            "mode": "a",
        },
    },
    "root": {
        "handlers": ["console", "debug_file_handler", "error_file_handler"],
        "level": "NOTSET",
    },
}

# Ensure directory structure exists
handlers = LOGGING_CONFIG["handlers"]
[
    Path(handlers[handler]["filename"]).parent.mkdir(exist_ok=True)
    for handler in handlers
    if handlers[handler]["class"] == "logging.FileHandler"
]

# Run once at startup:
logging.config.dictConfig(LOGGING_CONFIG)

# # Usage: include in each module:
# log = logging.getLogger(__name__)
# [
#     log.__getattribute__(lvl)(f"{lvl} logging is configured")
#     for lvl in ["debug", "info", "warning", "error", "critical"]
# ]
