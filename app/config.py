from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    HR_GROUP_ID: int
    PROXY_URL: Optional[str] = None

    # Recruitment Service integration — optional on purpose: if unset, the
    # bot just skips submission and keeps forwarding to HR_GROUP_ID as
    # before (see app/utils/recruitment.py).
    RECRUITMENT_SERVICE_URL: Optional[str] = None
    RECRUITMENT_SERVICE_TOKEN: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
