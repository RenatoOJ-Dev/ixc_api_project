import json
import requests
import os
from dotenv import load_dotenv


load_dotenv()


def fetch_ixc(grid_param: dict, rp: int = 100) -> dict:
    """
    chamada base para a API do IXC. Reutilizavel por qualquer módulo.
    """
    url = os.getenv('HOST__IXC__API')
    auth = os.getenv('TOKEN__IXC__API')

    headers = {
        'ixcsoft': 'listar',
        'Authorization': f'Basic {auth}'
    }

    payload = {
        "action": "grid",
        "page": "1",
        "rp": str(rp),
        "sortname": "su_oss_chamado.status",
        "sortorder": "desc",
        "grid_param": json.dumps(grid_param),
    }

    reponse = requests.post(str(url), headers=headers, data=payload)
    reponse.raise_for_status()

    return reponse.json()
