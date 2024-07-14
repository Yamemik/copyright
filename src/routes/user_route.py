from fastapi import APIRouter, status, Depends, HTTPException

from ..models.user_model import User
from ..schemas.user_schema import UserCreate, UserRead, UserUpdate
from ..services.user_service import auth_backend, current_active_user, fastapi_users

auth_router = APIRouter(
    prefix="/api/users",
    tags=["Пользователи"],
)


@auth_router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
