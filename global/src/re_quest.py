import requests
import base64
import os
from dotenv import load_dotenv
import json
from termcolor import colored
from time import sleep
# from winotify import Notification


load_dotenv()
host = os.getenv('HOST')

url = "https://{}/webservice/v1/su_oss_chamado".format(host)
token = "280:cd7817ba7c8f4c1afecfd882e01f996e4bd094e397015ed2f8349730ed4e21bd".encode('utf-8')
headers = {
    'ixcsoft': 'listar',
    'Authorization': 'Basic {}'.format(base64.b64encode(token).decode('utf-8')),
}


def get_tec_and_total_os(url: str, headers: dict) -> list:
    lista_de_tecnicos = [
        "RENAN GOMES",
        "GOBBO",
        "MICHEL",
        "SAULO",
        "DANILO",
        "EDER",
        "JHON",
        'KEVIN',
        'RODRIGO',
        # 'dalmo',
        # 'ivan',
        'RENATO'
    ]

    base_param = """[
        {
            "TB":"view_funcionarios_setor.funcionario","OP":"L","P":"#TEC#"
            },
        {
            "TB":"su_oss_chamado.status","OP":"IN","P":"\'A\',\'DS\',\'AN\',\'EX\',\'EN\',\'AS\',\'RAG\',\'AG\'"
            },
        {
            "TB":"su_oss_chamado.prioridade","OP":"IN","P":"\'B\',\'N\',\'A\',\'C\'"
            }
        ]"""
    list_message = []
    for tec in lista_de_tecnicos:
        payload = {
            'action': 'grid',
            'oper': 'L',
            'page': '1',
            'rp': '20',
            'sortname': 'su_oss_chamado.id',
            'sortorder': 'desc',
            'grid_param': base_param.replace('#TEC#', tec)
        }
        response = requests.post(url, headers=headers, data=payload)
        response_string = json.loads(response.text)
        total = response_string.get('total', 0)
        message = {
            'Tecnico': tec,
            'Total_os': total
        }
        list_message.append(message)
    return list_message


count = 1
value_count = 200
while count != value_count:
    list_message = get_tec_and_total_os(url=url, headers=headers)
    os.system('clear')
    dados_string = list_message
    for dado in dados_string:
        tecnico = dado.get('Tecnico')
        total_os = dado.get('Total_os')
        if total_os < 2:
            print(f'{colored(tecnico, "red")}: {colored(total_os, "red")}')
            print(10 * '---')

        else:
            print(f'{colored(tecnico, "blue")}: {colored(total_os, "green")}')
            print(10 * '---')

    count += 1
    value_count += 1
    print(f'Session:{colored(count, 'red')} Filnalizada')
    sleep(10)
