import os

import requests
from dotenv import load_dotenv

load_dotenv()
DEPLOYMENT_URL = os.getenv("DEPLOYMENT_URL")
CUIT = os.getenv("CUIT")
TOKEN = os.getenv("TOKEN")

def fe_param_get_cotization():

    url = f"{DEPLOYMENT_URL}/wsfe/FEParamGetCotizacion"

    data = {
        "Auth": {
            "Cuit": CUIT
        },
        "MonId" : "PES"
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

response = fe_param_get_cotization()
print(response)
