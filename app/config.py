from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    database_hostname: str
    database_name: str
    database_port: str
    database_password: str
    database_username: str
    openai_key: str = "default_value_if_missing"

    class config:
        env_file = os.path.join(os.path.dirname(__file__), ".env")


settings = Settings()
