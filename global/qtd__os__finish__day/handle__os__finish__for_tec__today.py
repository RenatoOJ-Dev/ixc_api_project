from raw__os__finish__for__tec__today import get__os__finish__for__tec__today


def reponse__finished__today():

    data__raw = get__os__finish__for__tec__today()
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
    count = 0
    dados__tratados = []
    for data in data__raw:
        f = {
            'Técnico': lista_de_tecnicos[count],
            'Total': data.get('total', 'null')
        }
        dados__tratados.append(f)
        count += 1

    return dados__tratados
