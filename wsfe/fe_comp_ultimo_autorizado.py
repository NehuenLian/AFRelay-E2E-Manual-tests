import os

import requests
from dotenv import load_dotenv

load_dotenv()
DEPLOYMENT_URL = os.getenv("DEPLOYMENT_URL")
CUIT = os.getenv("CUIT")
TOKEN = os.getenv("TOKEN")

def fe_comp_ultimo_autorizado():

    url = f"{DEPLOYMENT_URL}/wsfe/FECompUltimoAutorizado"

    data = {
        "Auth": {
            "Cuit": CUIT
        },
        "PtoVta": 1,
        "CbteTipo": 6
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

response = fe_comp_ultimo_autorizado()
print(response)