import json
import requests
from time import sleep
import os
from termcolor import colored
import tkinter as tk


url = "https://central.nv7.net.br/webservice/v1/su_oss_chamado"
auth = 'Basic MjgwOmNkNzgxN2JhN2M4ZjRjMWFmZWNmZDg4MmUwMWY5OTZlNGJkMDk0ZTM5NzAxNWVkMmY4MzQ5NzMwZWQ0ZTIxYmQ='
root = tk.Tk()


def tec_total(auth: str, url: str) -> list:
    headers = {
        'ixcsoft': 'listar',
        'Authorization': auth
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

    grid_param = [
        {
            "TB": "view_funcionarios_setor.funcionario",
            "OP": "L",
            "P": 'danilo'
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
    r = requests.post(url, headers=headers, data=payload)
    dados = r.json()
    total = dados.get('total', 0)
    
    message = {
        # 'tecnico': tec,
        'total': total,
    }
    lib_os.append(message)
    return (lib_os, dados)

dados, registro = tec_total(auth, url)

print(registro)
# for reg in registro['registros']:
#     print(dados)
#     endereco = reg.get('endereco', [])
#     latitude = reg.get('latitude', [])
#     longitude = reg.get('longitude', [])
#     cliente_id = reg.get('id_cliente', [])
#     print(endereco, latitude, longitude, cliente_id)
#     print(reg)
