from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # common
    app_name: str = "copyright"
    debug: bool = True

    # db
    url: str = "postgresql+asyncpg://postgres:postgres@localhost/postgres"

    # auth
    secret: str = "B$j8VpWY@rL&J0$$"


settings = Settings()
