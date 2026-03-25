import os

import requests
from dotenv import load_dotenv

load_dotenv()

DEPLOYMENT_URL = os.getenv("DEPLOYMENT_URL")
CUIT = os.getenv("CUIT")
TOKEN = os.getenv("TOKEN")

def fecaea_solicitar():

    url = f"{DEPLOYMENT_URL}/wsfev1/FECAEASolicitar"

    data = {
        "Auth": {
            "Cuit": CUIT
        },
        "Periodo": 202603,
        "Orden": 2
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

response = fecaea_solicitar()
print(response)