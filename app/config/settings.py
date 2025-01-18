import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    RAPIDAPI_KEY: str = os.getenv("RAPIDAPI_KEY")

settings = Settings()
