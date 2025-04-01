from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Carrega o .env
load_dotenv()


class Settings(BaseSettings):
    API_KEY: str 
    CHAT_URL: str
    HOST: str
    API_PORT: int

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()