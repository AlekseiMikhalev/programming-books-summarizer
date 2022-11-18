from fastapi import FastAPI, Depends
from users.controllers import admin, readings
from configuration.config import UsersSettings, ServerSettings

users_app = FastAPI()
users_app.include_router(admin.router)
users_app.include_router(readings.router)


def build_config():
    return UsersSettings()


def fetch_config():
    return ServerSettings()


@users_app.get('/index')
def index_users(config: UsersSettings = Depends(build_config), fconfig: ServerSettings = Depends(fetch_config)):
    return {
        'project_name': config.application,
        'webmaster': config.webmaster,
        'created': config.created,
        'development_server': fconfig.development_server,
        'development_port': fconfig.development_port
    }
