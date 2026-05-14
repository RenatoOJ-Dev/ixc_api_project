import json
import requests
from time import sleep
import os
from dotenv import load_dotenv


load_dotenv()  # **/ Leitura das variables dentro do .env


def acess_direct_api() -> dict:
    '''
    Retorna os valores crus mandandos pela API do IXC
    '''

    url: str | bytes = str(os.getenv('HOST__IXC__API'))
    auth: str | None = 'Basic MjgwOmNkNzgxN2JhN2M4ZjRjMWFmZWNmZDg4MmUwMWY5OTZlNGJkMDk0ZTM5NzAxNWVkMmY4MzQ5NzMwZWQ0ZTIxYmQ='

    # **/ Padrão de tabela dado pela API do IXC para consulta
    headers = {
        'ixcsoft': 'listar',
        'Authorization': auth
    }

    grid_param = {
        "0": {
            "TB": "funcionarios.funcionario",
            "display": "Colaborador",
            "OP": "L",
            "P": "renato",
            "C": "AND",
            "G": "_funcionarios.funcionario"
        },
        "1": {
            "TB": "su_oss_chamado.status",
            "display": "Status",
            "OP": "IN",
            "P": "\"A\",\"EN\"",
            "C": "AND",
            "G": "_su_oss_chamado.status"
        },
        "2": {
            "TB": "su_oss_assunto.assunto",
            "display": "Assunto",
            "OP": "L",
            "P": "reparo",
            "C": "AND",
            "G": "_su_oss_assunto.assunto"
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
    return dados
