import json
import requests
from time import sleep
import os
from termcolor import colored
# import tkinter as tk


url = "https://central.nv7.net.br/webservice/v1/su_oss_chamado"
auth = 'Basic MjgwOmNkNzgxN2JhN2M4ZjRjMWFmZWNmZDg4MmUwMWY5OTZlNGJkMDk0ZTM5NzAxNWVkMmY4MzQ5NzMwZWQ0ZTIxYmQ='


def tec_total(auth: str, url: str) -> list:
    headers = {
        'ixcsoft': 'listar',
        'Authorization': auth
    }
    lista_de_tecnicos = [
        "RENAN GOMES",
        "GOBBO",
        
        "MICHEL",
        "SAULO",
        
        "DANILO",
        "EDER",
        
        "JHON",
        'KEVIN',
        
        # 'DALMO',
        
        # "RENATO",
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
        r = requests.post(url, headers=headers, data=payload)
        dados = r.json()
        total = dados.get('total', 0)
        message = {
            'tecnico': tec,
            'total': total
        }
        lib_os.append(message)
    return lib_os


count = 0
inf = 100
while count != inf:
    r = tec_total(auth, url)
    os.system('clear')
    for i in r:
        nome = i.get('tecnico', '')
        total_os = i.get('total', 0)
        if total_os < 2:
            print(f'{colored(text=str(nome), color='red')} -------- {colored(text=str(total_os), color='red')}')
            print(10 * '___')

        else:
            print(f'{colored(text=str(nome), color='green')} -------- {colored(text=str(total_os), color='yellow')}')
            print(10 * '___')

    count += 1
    inf += 1
    print(count, inf)
    sleep(10)
