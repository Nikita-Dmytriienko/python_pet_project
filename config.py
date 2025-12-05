import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

print("Current dir:", os.getcwd())
print("root .env", env_path)
print("Load .env:", load_dotenv(dotenv_path=env_path)) #True of False
print("GEMINI_API_KEY loaded:", bool(os.getenv("GEMINI_API_KEY"))) #++

class Config:
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY doesnt found in .env !")

config_obj = Config()