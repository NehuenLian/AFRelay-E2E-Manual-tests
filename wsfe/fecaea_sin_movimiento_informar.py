import os

import requests
from dotenv import load_dotenv

load_dotenv()

DEPLOYMENT_URL = os.getenv("DEPLOYMENT_URL")
CUIT = os.getenv("CUIT")
TOKEN = os.getenv("TOKEN")

def fecaea_sin_movimiento_informar():

    url = f"{DEPLOYMENT_URL}/wsfe/FECAEASinMovimientoInformar"

    data = {
        "Auth": {
            "Cuit": CUIT
        },
        "PtoVta": 1,
        "CAEA": "86060007329748"
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

response = fecaea_sin_movimiento_informar()
print(response)