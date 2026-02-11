import os

import requests
from dotenv import load_dotenv

from common import get_date_today

load_dotenv()
DEPLOYMENT_URL = os.getenv("DEPLOYMENT_URL")
CUIT = os.getenv("CUIT")
TOKEN = os.getenv("TOKEN")

def fecae_reg_informativo():

    url = f"{DEPLOYMENT_URL}/wsfe/FECAEARegInformativo"

    payload = {
        "Auth": {
            "Cuit": CUIT
        },
        "FeCAEARegInfReq": {
            "FeCabReq": {
                "CantReg": 1,
                "PtoVta": 1,
                "CbteTipo": 1
            },
            "FeDetReq": {
                "FECAEADetRequest": [
                    {
                        "Concepto": 1,
                        "DocTipo": 99,
                        "DocNro": 20123456789,
                        "CbteDesde": 1,
                        "CbteHasta": 1,
                        "CbteFch": get_date_today(),
                        "ImpTotal": 121.00,
                        "ImpTotConc": 0.00,
                        "ImpNeto": 100.00,
                        "ImpOpEx": 0.00,
                        "ImpIVA": 21.00,
                        "ImpTrib": 0.00,
                        "MonId": "PES",
                        "MonCotiz": 1.00,
                        "CondicionIVAReceptorId": 1,
                        "CAEA": "12345678901234"
                    }
                ]
            }
        }
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

response = fecae_reg_informativo()
print(response)