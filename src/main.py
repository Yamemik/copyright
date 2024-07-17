from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.common.settings import settings
from src.common.database import create_db_and_tables
from src.routes.feedback_route import feedback_router
from src.routes.course_route import course_router

from src.schemas.user_schema import UserCreate, UserRead, UserUpdate
from src.services.user_service import auth_backend, fastapi_users, current_active_user


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


def create_app():
    app = FastAPI(
        debug=settings.debug,
        docs_url="/api/docs",
        title=f"{settings.app_name} API docs",
        lifespan=lifespan,
    )

    origins = [
        "https://copyright-chu.ru/",
        "http://copyright-chu.ru/",
        "http://localhost",
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(
        fastapi_users.get_auth_router(auth_backend), prefix="/api/auth/jwt", tags=["auth"]
    )
    app.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/api/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_reset_password_router(),
        prefix="/api/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_verify_router(UserRead),
        prefix="/api/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_users_router(UserRead, UserUpdate),
        prefix="/api/users",
        tags=["users"],
    )

    app.include_router(feedback_router, dependencies=[Depends(current_active_user)])
    app.include_router(course_router, dependencies=[Depends(current_active_user)])

    return app
