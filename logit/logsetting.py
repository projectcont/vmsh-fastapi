import logging
import logging.config
import traceback
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
path_to_log_file = BASE_DIR.joinpath('logit/events.log')


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_format': {
            "format": "{asctime} - {levelname} - {module} - {filename}- {message} ",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "main_format",
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "main_format",
            "filename": path_to_log_file,
        }

    },
    "loggers": {
        "main": {
            "handlers": ['file',],
            "level": "INFO",
            "propagate": "True",
        }

    },

}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('main')

