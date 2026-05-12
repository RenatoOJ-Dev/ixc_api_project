import json
import requests
from time import sleep
import os
from termcolor import colored
# import tkinter as tk


url = "https://central.nv7.net.br/webservice/v1/su_oss_chamado"
auth = 'Basic MjgwOmNkNzgxN2JhN2M4ZjRjMWFmZWNmZDg4MmUwMWY5OTZlNGJkMDk0ZTM5NzAxNWVkMmY4MzQ5NzMwZWQ0ZTIxYmQ='


def tec_total(auth: str, url: str) -> dict:
    headers = {
        'ixcsoft': 'listar',
        'Authorization': auth
    }

    grid_param = [
        {
            "TB": "su_oss_chamado.data_agenda", "OP": "BE", "P": "2026-05-12 00:00:00", "P2": "2026-05-12 23:59:59"
        },
        {
            "TB": "view_funcionarios_setor.funcionario", "OP": "L", "P": "renato"},
        {
            "TB": "su_oss_chamado.status", "OP": "IN", "P": "'A','DS','AN','EX','EN','AS','RAG','AG'"
        },
        {
            "TB": "su_oss_assunto.assunto", "OP": "L", "P": "reparo"},
        {
            "TB": "su_oss_chamado.prioridade", "OP": "IN", "P": "'B','N','A','C'"
        }
    ]
    grid_param_string = json.dumps(grid_param)
    payload = {
        'action': 'grid',
        'page': '1',
        'rp': '10',
        'sortname': 'su_oss_chamado.status',
        'sortorder': 'desc',
        'grid_param': grid_param_string
    }
    r = requests.post(url, headers=headers, data=payload)
    dados = r.json()
    return dados


request = tec_total(auth, url)
print(type(request))
registors = request.get('registros', '')
for i in registors:
    print(i, end='\n')
