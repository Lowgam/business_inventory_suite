# Module: settings.py
# Purpose: technical application data

from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from functools import lru_cache

BASE_DIR = Path(__file__).resolve().parents[3]
ENV_FILE = BASE_DIR / ".env.development"

class Settings(BaseSettings):
    environment : str
    database_url : str
    redis_url : str
    session_secret : str
    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")

@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    return settings
