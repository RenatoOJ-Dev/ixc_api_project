import os
from dotenv import load_dotenv

load_dotenv()

type Array = list
type String = str

TECNICOS: dict[int, String] = os.getenv('TECNICOS')

NOMES_TECNICOS = os.getenv('NOMES_TECNICOS')


def get_nome_tecnico(id_tecnico) -> str:
    try:
        return TECNICOS.get(int(id_tecnico), f"Técnico #{id_tecnico}")
    except (ValueError, TypeError):
        return f"Técnico #{id_tecnico}"
