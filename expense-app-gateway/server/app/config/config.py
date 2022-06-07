import logging
import sys
from typing import List
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
from app.config.logging import InterceptHandler
import os
BASE_PATH = os.path.dirname(__file__)
SECRET_SEED_KEY = "secret"
JWT_SECRET_KEY = 'dQeyjj5YvqCRdP6C8EH47FTmKDg6yPE0'
API_PREFIX = "/api"
JWT_TOKEN_PREFIX = "Token" 
VERSION = "0.0.0"
config = Config(".env")
DEBUG: bool = config("DEBUG", cast=bool, default=True)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret , default="Distar-GPS-Server-Key")
PROJECT_NAME: str = config("Distar-GPS-Server", default="Distar-GPS-Server")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)
# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
