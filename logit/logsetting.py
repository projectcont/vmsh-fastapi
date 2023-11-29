import logging
import logging.config
import traceback

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
            "filename": "logit/events.log",
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

