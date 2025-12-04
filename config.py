import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY doesnt found in .env !")

config_obj = Config()