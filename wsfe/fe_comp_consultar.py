import os

import requests
from dotenv import load_dotenv

load_dotenv()
DEPLOYMENT_URL = os.getenv("DEPLOYMENT_URL")
CUIT = os.getenv("CUIT")
TOKEN = os.getenv("TOKEN")

def fe_comp_consultar():

    url = f"{DEPLOYMENT_URL}/wsfe/FECompConsultar"

    data = {
        "Auth": {
            "Cuit": CUIT
        },
        "FeCompConsReq": {
            "PtoVta": 1,
            "CbteTipo": 6,
            "CbteNro": 100,
        }
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

response = fe_comp_consultar()
print(response)
