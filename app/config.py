"""Config file for project"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Class settings from pydantic. Similar as dotenv"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    db_host: str = ""
    db_port: str = ""
    db_name: str = ""
    db_user: str = ""
    db_pass: str = ""


settings = Settings()
