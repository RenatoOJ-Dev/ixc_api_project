import json
import requests
from time import sleep
import os
from termcolor import colored
import tkinter as tk


url = "https://central.nv7.net.br/webservice/v1/su_oss_chamado"
auth = 'Basic MjgwOmNkNzgxN2JhN2M4ZjRjMWFmZWNmZDg4MmUwMWY5OTZlNGJkMDk0ZTM5NzAxNWVkMmY4MzQ5NzMwZWQ0ZTIxYmQ='

app = tk.Tk()
app.title('Fingerprint')
app.geometry('300x500')


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


main_label = tk.Label(app, text='Informações', font=('Arial', 16), bg='pink')
visual_frame = tk.Frame(app)
info_label = tk.Label(visual_frame, text='', font=('Arial', 12))
btn = tk.Button(app, text='START', font=('Arial', 14), command=lambda: atualizar_dados())

info_label.pack(side='top')
main_label.pack(pady=20)
btn.pack()
visual_frame.pack(expand=True, fill='both')


def atualizar_dados():
    r = tec_total(auth, url)
    linhas = []
    for i in r:
        nome = i.get('tecnico', '')
        total_os = i.get('total', 0)

        if total_os < 2:
            linhas.append(f"\n{nome} -------- {total_os} (ATENÇÃO)")
        else:
            linhas.append(f"\n{nome} -------- {total_os}")
    info_label.config(text="\n".join(linhas) if linhas else "Nenhum dado retornado.", justify='center')
    app.after(10000, atualizar_dados)


app.mainloop()
