import json
import requests
from time import sleep
import os
from dotenv import load_dotenv


load_dotenv()  # **/ Leitura das variables dentro do .env


def acess_direct_api__ex() -> dict:
    '''
    Retorna os valores crus mandandos pela API do IXC
    '''

    url: str | bytes = str(os.getenv('HOST_IXC_URL'))
    auth: str | None = os.getenv('TOKEN_IXC_ACESS')

    # **/ Padrão de tabela dado pela API do IXC para consulta
    headers = {
        'ixcsoft': 'listar',
        'Authorization': auth
    }

    grid_param = {
        "0":
        {
            "TB": "su_oss_chamado.status", "display": "Status", "OP": "IN", "P": "\"EX\"", "C": "AND", "G": "_su_oss_chamado.status"
        }
    }

    grid_param_string = json.dumps(grid_param)
    payload = {
        'action': 'grid',
        'page': '1',
        'rp': '100',
        'sortname': 'su_oss_chamado.status',
        'sortorder': 'desc',
        'grid_param': grid_param_string
    }

    r = requests.post(url, headers=headers, data=payload)
    dados: dict = r.json()
    list__items__api = normalize__api__data(dados)
    return list__items__api


def normalize__api__data(data__raw):
    data__total = data__raw.get('total', 0)
    if data__raw:
        list__items__api = [{
            'id_tecnico': data.get('id_tecnico'),
            'id_cliente': data.get('id_cliente'),
            'id_assunto': data.get('id_assunto'),
            'endereco': data.get('endereco')
        }for data in data__raw.get('registros')]

    return list__items__api
