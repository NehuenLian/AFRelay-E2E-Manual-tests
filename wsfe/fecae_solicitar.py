import os

import requests
from dotenv import load_dotenv

from common import get_date_today

load_dotenv()
DEPLOYMENT_URL = os.getenv("DEPLOYMENT_URL")
CUIT = os.getenv("CUIT")
TOKEN = os.getenv("TOKEN")


def fecae_solicitar():

    url = f"{DEPLOYMENT_URL}/wsfe/FECAESolicitar"

    payload = {
        "Auth": {
            "Cuit": CUIT
        },
        "FeCAEReq": {
            "FeCabReq": {
                "CantReg": 1,
                "PtoVta": 1,
                "CbteTipo": 11
            },
            "FeDetReq": {
                "FECAEDetRequest": [
                    {
                        "Concepto": 1,
                        "DocTipo": 99,
                        "DocNro": 0,
                        "CbteDesde": 2,
                        "CbteHasta": 2,
                        "CbteFch" : get_date_today(),
                        "ImpTotal": 100.0,
                        "ImpNeto": 100.0,
                        "ImpTotConc": 0.0,
                        "ImpOpEx": 0.0,
                        "ImpTrib": 0.0,
                        "ImpIVA": 0.0,
                        "MonId": "PES",
                        "MonCotiz": 1,
                        "CondicionIVAReceptorId": 5,
                    }
                ]
            }
        }
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.post(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()

response = fecae_solicitar()
print(response)