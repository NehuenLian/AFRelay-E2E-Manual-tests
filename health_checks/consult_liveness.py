import os

import requests
from dotenv import load_dotenv

load_dotenv()
DEPLOYMENT_URL = os.getenv("DEPLOYMENT_URL")

def liveness() -> dict | None:

    url = f"{DEPLOYMENT_URL}/health/liveness"

    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

response = liveness()
print(response)