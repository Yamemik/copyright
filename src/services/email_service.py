from typing import List

from pydantic import EmailStr, BaseModel

from fastapi_mail import FastMail, MessageSchema, MessageType

from ..email.config import conf


class EmailSchema(BaseModel):
    email: List[EmailStr]


async def create_message_after_reg(email: EmailSchema):
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),
        boby="""<p>Hi this test mail, thanks for using Fastapi-mail</p> """,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)


