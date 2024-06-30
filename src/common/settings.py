from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # common
    app_name: str = "copyright"
    debug: bool = True

    # db
    url: str = "postgresql://postgres:postgres@localhost/postgres"


settings = Settings()
