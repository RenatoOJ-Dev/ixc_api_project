from datetime import date
from api.client import fetch_ixc
from api.tecnicos import NOMES_TECNICOS


def _build_grid_param(nome_tecnico: str, data: date) -> dict:
    data_str = data.strftime("%Y-%m-%d")
    return {
        "0": {
            "TB": "su_oss_chamado.status",
            "display": "Status",
            "OP": "IN",
            "P": '"F"',
            "C": "AND",
            "G": "_su_oss_chamado.status",
        },
        "1": {
            "TB": "su_oss_chamado.data_fechamento",
            "display": "Fechamento",
            "OP": "BE",
            "P": f"{data_str} 00:00:00",
            "P2": f"{data_str} 23:59:59",
            "C": "AND",
            "G": "_su_oss_chamado.data_fechamento",
        },
        "2": {
            "TB": "funcionarios.funcionario",
            "display": "Colaborador",
            "OP": "L",
            "P": nome_tecnico,
            "C": "AND",
            "G": "_funcionarios.funcionario",
        },
    }


def fetch_os_finalizadas_hoje(data: date | None = None) -> list[dict]:
    """Busca OS finalizadas hoje para cada técnico."""
    data = data or date.today()
    resultados = []

    for tecnico in NOMES_TECNICOS:
        grid_param = _build_grid_param(tecnico, data)
        try:
            resultado = fetch_ixc(grid_param, rp=24)
            resultados.append(resultado)

        except Exception as e:
            print(f'Erro ao buscar OS de {tecnico}: {e}')
            resultados.append({})

    return resultados
