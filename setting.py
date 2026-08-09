import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def get_openai_api_key(self) -> str:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        return api_key

config = Config()