from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

from src.common.settings import settings
from src.common.database import create_db_and_tables

from src.schemas.user_schema import UserCreate, UserRead, UserUpdate
from src.services.user_service import auth_backend, fastapi_users


@asynccontextmanager
async def lifespan(app: FastAPI):
	# Not needed if you setup a migration system like Alembic
	await create_db_and_tables()
	yield


def create_app():
	app = FastAPI(
		debug=settings.debug,
		docs_url="/api/docs",
		title=f"{settings.app_name} API docs",
		lifespan=lifespan,
	)

	app.include_router(
		fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
	)
	app.include_router(
		fastapi_users.get_register_router(UserRead, UserCreate),
		prefix="/auth",
		tags=["auth"],
	)
	app.include_router(
		fastapi_users.get_reset_password_router(),
		prefix="/auth",
		tags=["auth"],
	)
	app.include_router(
		fastapi_users.get_verify_router(UserRead),
		prefix="/auth",
		tags=["auth"],
	)
	app.include_router(
		fastapi_users.get_users_router(UserRead, UserUpdate),
		prefix="/users",
		tags=["users"],
	)

	return app
