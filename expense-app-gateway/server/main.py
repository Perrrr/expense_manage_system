import sys
from app.core.server import get_application
from loguru import logger


version = f"{sys.version_info.major}.{sys.version_info.minor}"


app = get_application() 
logger.info(f"application start - {version}" )
