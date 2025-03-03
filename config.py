import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # General settings
    PROJECT_NAME = "FastAPI MVC App"
    VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1"]

    # Database settings

    # Security settings
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # Cache settings
    CACHE_MAX_SIZE = int(os.getenv("CACHE_MAX_SIZE", 100))
    CACHE_TTL = int(os.getenv("CACHE_TTL", 300))

config = Config()
