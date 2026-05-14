import json
import requests
from time import sleep
import os
from termcolor import colored
import base64


url = "https://central.nv7.net.br/webservice/v1/su_oss_chamado"
auth = '93:d9762a57d0e91d60f723cf042a2eada10367467d463a13288ce21bad6f25aeb3'.encode('utf-8')


def tec_total(auth, url: str) -> str:
    headers = {
        'ixcsoft': 'listar',
        'Authorization': 'Basic {}'.format(base64.b64encode(auth).decode('utf-8')),
    }
    lista_de_tecnicos = [
        "renan gomes",
        "gobbo",
        "wesley",
        "michel",
        "saulo",
        "danilo",
        "eder",
        "jhon",
        "marcelo",
        "renato"
    ]

    lib_os = []
    for tec in lista_de_tecnicos:
        grid_param = [
            {
                "TB": "view_funcionarios_setor.funcionario",
                "OP": "L",
                "P": 'renato'
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
            'rp': '100',  # ← Aumentei de 1 para 20 para pegar mais OS
            'sortname': 'su_oss_chamado.id',
            'sortorder': 'desc',
            'grid_param': grid_param_string
        }
        r = requests.post(url, headers=headers, data=payload)
        # dados = r
    return r.text


data = tec_total(auth, url)
print(data)
