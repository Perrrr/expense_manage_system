
from fastapi import FastAPI 
from starlette.middleware.cors import CORSMiddleware
from app.config.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from fastapi.staticfiles import StaticFiles
from app.handler.api import router as api_router
import logging


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION )
    create_static_folder_if_not_exist()
    application.mount("/static", StaticFiles(directory="app/static"), name="static")
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
   
    application.include_router(api_router, prefix=API_PREFIX)
    return application

def create_static_folder_if_not_exist():
    import os
    if not os.path.exists("app/static"):
        os.makedirs("app/static")
        os.makedirs("app/static/public")
        os.makedirs("app/static/private")
