from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from ..services.email_service import create_message_after_reg, EmailSchema


email_router = APIRouter(
    prefix="/api/email",
    tags=["Почта"],
)


@email_router.post(
    "/send",
    summary="Отправить сообщение",
    status_code=status.HTTP_202_ACCEPTED
)
async def simple_send(email: EmailSchema) -> JSONResponse:
    await create_message_after_reg(email)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
