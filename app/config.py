"""
Created by Epic at 7/8/20
"""
from os import environ as env
import logging

logger = logging.getLogger("api.config")


def bool_converter(text: str) -> bool:
    if isinstance(text, bool):
        return text
    values = {
        "true": True,
        "false": False
    }

    value = values.get(text, None)
    if value is None:
        raise ValueError(f"Invalid config value. Expected true or false")
    return value


try:
    DEBUG = bool_converter(env.get("debug", True))
    DATABASE_URI = env["database_uri"]
    API_TOKEN = env["api_token"]
except KeyError as e:
    logger.critical(f"Missing required config values. Missing setting: {e.args[0]}")
    raise SystemExit()
