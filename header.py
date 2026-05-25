import os
import logging
import httpx
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
API_KEY_OF_OPENWEATHER = os.getenv("OPENWEATHER_API_KEY")

logging.basicConfig(
    filename="my_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

client = httpx.Client()

class WeatherMonitor(BaseModel):
    city: str
    temperature: float
    description: str
