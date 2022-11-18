from pydantic import BaseSettings
from datetime import date
import os


class LibrarySettings(BaseSettings):
    application: str = 'Library Management Service'
    webmaster: str = 'mikhalev.aleksei1@gmail.com'
    created: date = '2022-11-20'


class UsersSettings(BaseSettings):
    application: str = 'Users Management Service'
    webmaster: str = 'mikhalev.aleksei1@gmail.com'
    created: date = '2022-11-20'


class SummarizerSettings(BaseSettings):
    application: str = 'Programming Books Summarization Service'
    webmaster: str = 'mikhalev.aleksei1@gmail.com'
    created: date = '2022-11-20'


class ServerSettings(BaseSettings):
    production_server: str
    production_port: int
    development_server: str
    development_port: int

    class Config:
        env_file = os.getcwd() + '/configuration/prog_books_app_settings.properties'
