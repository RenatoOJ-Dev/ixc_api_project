from api.client import fetch_ixc
from api.tecnicos import get_nome_tecnico


GRID_PARAM_EM_EXECUCAO = {
    "0": {
        "TB": "su_oss_chamado.status",
        "display": "Status",
        "OP": "IN",
        "P": '"EX"',
        "C": "AND",
        "G": "_su_oss_chamado.status",
    }
}


def fetch_os_em_execucao() -> list | None:
    try:
        data = fetch_ixc(grid_param=GRID_PARAM_EM_EXECUCAO)
        registros = data.get('registros')
        if not registros:
            return None
        return parse_os_execucao(registros)
    except Exception as e:
        print(f'Erro ao buscar OS em execução: {e}')
        return None


def parse_os_execucao(registros: list) -> list:
    return [
        {
            'tecnico': get_nome_tecnico(item.get('id_tecnico')),
            "id_cliente": item.get("id_cliente"),
            "id_assunto": item.get("id_assunto"),
            "endereco": item.get("endereco"),
        } for item in registros
    ]
