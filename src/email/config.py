from fastapi_mail import ConnectionConfig

conf = ConnectionConfig(
    MAIL_USERNAME="copyright2024@mail.ru",
    MAIL_PASSWORD="Gn1pbxVDnefCK0eHDRWH",
    #MAIL_PASSWORD="6gAnimed-skvayr8-antonina",
    MAIL_FROM="copyright2024@mail.ru",
    MAIL_PORT=65,
    MAIL_SERVER="smtp.mail.ru",
    MAIL_FROM_NAME="copyright2024@mail.ru",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)
