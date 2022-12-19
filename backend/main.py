from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.router import router as auth_router
from database.session import engine
from config import get_settings
from library.router import router as library_router
from users.router import router as users_router

from users.models import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_routers(app):
    app.include_router(auth_router)
    app.include_router(users_router)
    app.include_router(library_router)


def start_application():
    app = FastAPI(title=get_settings().project_title,
                  version=get_settings().project_version)
    app.middleware("http")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            origin for origin in get_settings().backend_cors_origins
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    create_tables()
    include_routers(app)

    return app


book_summarizer_app = start_application()
