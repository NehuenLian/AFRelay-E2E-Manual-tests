import os

import requests
from dotenv import load_dotenv

load_dotenv()
DEPLOYMENT_URL = os.getenv("DEPLOYMENT_URL")
CUIT = os.getenv("CUIT")
TOKEN = os.getenv("TOKEN")

def fe_param_get_condicion_iva_receptor():

    url = f"{DEPLOYMENT_URL}/wsfe/FEParamGetCondicionIvaReceptor"

    data = {
        "Auth": {
            "Cuit": CUIT
        },
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

response = fe_param_get_condicion_iva_receptor()
print(response)
