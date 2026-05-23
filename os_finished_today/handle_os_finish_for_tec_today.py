from api.tecnicos import NOMES_TECNICOS
from .raw_os_finish_for_tec_today import fetch_os_finalizadas_hoje


def get_os_finalizadas_hoje() -> list[dict]:
    """Retorna total de OS finalizadas hoje por técnico."""
    raw = fetch_os_finalizadas_hoje()
    return [
        {
            "tecnico": tecnico,
            "total": data.get("total", 0),
        }
        for tecnico, data in zip(NOMES_TECNICOS, raw)
    ]
