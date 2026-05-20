import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get__os__finish__for__tec__today() -> list:
    url = os.getenv('HOST__IXC__API')
    auth: str | None = 'Basic MjgwOmNkNzgxN2JhN2M4ZjRjMWFmZWNmZDg4MmUwMWY5OTZlNGJkMDk0ZTM5NzAxNWVkMmY4MzQ5NzMwZWQ0ZTIxYmQ='

    headers = {
        'ixcsoft': 'listar',
        'Authorization': auth
    }
    lista_de_tecnicos = [
        "RENAN GOMES",

        "GOBBO",

        # "MICHEL",
        # "SAULO",
        "DANILO",
        "EDER",

        "JHON",
        'KEVIN',

        'RODRIGO',
    ]

    lib_os = []
    for tec in lista_de_tecnicos:
        grid_param = {
            "0":
            {"TB": "su_oss_chamado.status",
             "display": "Status",
             "OP": "IN",
             "P": "\"F\"",
             "C": "AND",
             "G": "_su_oss_chamado.status"
             },
            "1":
            {
                "TB": "su_oss_chamado.data_fechamento",
                "display": "Fechamento",
                "OP": "BE",
                "P": "2026-05-18 00:00:00",
                "P2": "2026-05-18 23:59:59",
                "C": "AND",
                "G": "_su_oss_chamado.data_fechamento"
            },
            "2":
            {
                "TB": "funcionarios.funcionario",
                "display": "Colaborador",
                "OP": "L",
                "P": tec,
                "C": "AND",
                "G": "_funcionarios.funcionario"
            }
        }
        grid_param_string = json.dumps(grid_param)
        payload = {
            'action': 'grid',
            'page': '1',
            'rp': '24',  # ← Aumentei de 1 para 20 para pegar mais OS
            'sortname': 'su_oss_chamado.id',
            'sortorder': 'desc',
            'qtype': 'su_oss_chamado.id',
            'oper': 'L',
            'grid_param': grid_param_string
        }

        r = requests.post(str(url), headers=headers, data=payload)
        dados = json.loads(r.text)
        lib_os.append(dados)
    return lib_os
