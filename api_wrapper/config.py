from dotenv import load_dotenv
import os

# load environment variables from .env file.
load_dotenv()

RIOT_API_KEY = os.getenv("RIOT_API_KEY")
RIOT_REGION = os.getenv("RIOT_REGION")
BASE_URL = f"https://{RIOT_REGION}.api.riotgames.com/"
