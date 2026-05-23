# qtd_os_tecnico.py

from api.client import fetch_ixc
from api.tecnicos import NOMES_TECNICOS
import logging


def _build_grid_param(nome_tecnico: str) -> list:
    return [
        {
            "TB": "view_funcionarios_setor.funcionario",
            "OP": "L",
            "P": nome_tecnico,
        },
        {
            "TB": "su_oss_chamado.status",
            "OP": "IN",
            "P": "'A','DS','AN','EX','EN','AS','RAG','AG'",
        },
    ]


def fetch_os_abertas_por_tecnico() -> list[dict]:
    """Retorna o total de OS abertas agrupado por técnico."""
    resultados = []

    if NOMES_TECNICOS:
        for tecnico in NOMES_TECNICOS:
            try:
                data = fetch_ixc((_build_grid_param(tecnico)), rp=24)
                resultados.append({
                    "tecnico": tecnico,
                    "total": data.get("total", 0),
                })

            except Exception as e:
                logging.error(f'Erro ao buscar OS de {tecnico}:{e}')
                resultados.append({"tecnico": tecnico, "total": 0})
        return resultados
    return resultados
