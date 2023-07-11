# encoding: utf-8
"""Encapsula a criação do logger da aplicação."""
import logging
from logging.config import dictConfig

log_format = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        },
        "json_formatter": {
            "class": "flask_google_cloud_logger.FlaskGoogleCloudFormatter",
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        },
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
        "json": {
            "class": "logging.StreamHandler",
            "formatter": "json_formatter",
        },
    },
    "loggers": {
        "root": {"level": "INFO", "handlers": ["json"]},
    },
}

dictConfig(log_format)

LOGGER = logging.getLogger("root")
