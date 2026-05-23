
from dotenv import load_dotenv
from .status import get_nome_status
from api.client import fetch_ixc

load_dotenv()

GRID_PARAM_RENATO = {
    "0": {
        "TB": "funcionarios.funcionario",
        "display": "Colaborador",
        "OP": "L",
        "P": "renato",
        "C": "AND",
        "G": "_funcionarios.funcionario",
    },
    "1": {
        "TB": "su_oss_chamado.status",
        "display": "Status",
        "OP": "IN",
        "P": '"A","EN"',
        "C": "AND",
        "G": "_su_oss_chamado.status",
    },
    "2": {
        "TB": "su_oss_assunto.assunto",
        "display": "Assunto",
        "OP": "L",
        "P": "reparo",
        "C": "AND",
        "G": "_su_oss_assunto.assunto",
    },
}


def parse_registros(registros: list) -> list:
    """Transforma os registros brutos no formato usado pela view."""
    return [
        {
            "bairro": item.get("bairro", ""),
            "status": get_nome_status(item.get("status")),
            "mensagem": item.get("mensagem", ""),
        }
        for item in registros
    ]


def get_os_renato() -> list | None:
    """Retorna as OS do Renato já tratadas, ou None se vazio."""
    try:
        data = fetch_ixc(grid_param=GRID_PARAM_RENATO)
        registros = data.get("registros")
        if not registros:
            return None
        return parse_registros(registros)
    except Exception as e:
        print(f"Erro ao buscar OS: {e}")
        return None
