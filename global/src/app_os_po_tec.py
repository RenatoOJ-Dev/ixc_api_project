import json
import requests
from time import sleep
import os
from termcolor import colored
# import tkinter as tk
from dotenv import load_dotenv

load_dotenv()


def tec_total() -> list:
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

        'DALMO',
        'RODRIGO',
        "RENATO",
    ]

    lib_os = []
    for tec in lista_de_tecnicos:
        grid_param = [
            {
                "TB": "view_funcionarios_setor.funcionario",
                "OP": "L",
                "P": tec
            },
            {
                "TB": "su_oss_chamado.status",
                "OP": "IN",
                "P": "'A','DS','AN','EX','EN','AS','RAG','AG'"
            }
        ]
        grid_param_string = json.dumps(grid_param)
        payload = {
            'action': 'grid',
            'page': '1',
            'rp': '10',  # ← Aumentei de 1 para 20 para pegar mais OS
            'sortname': 'su_oss_chamado.id',
            'sortorder': 'desc',
            'grid_param': grid_param_string
        }
        r = requests.post(str(url), headers=headers, data=payload)
        dados = r.json()
        total = dados.get('total', 0)
        message = {
            'tecnico': tec,
            'total': total
        }
        lib_os.append(message)
    return lib_os
