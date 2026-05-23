STATUS: dict[str, str] = {
    "A": "Aberta",
    "AN": "Análise",
    "EN": "Encaminhada",
    "AS": "Assumida",
    "AG": "Agendada",
    "DS": "Deslocamento",
    "EX": "Execução",
    "F": "Finalizada",
    "RAG": "Aguardando Agendamento",
}


def get_nome_status(status) -> str:
    return STATUS.get(str(status), f"Status #{status}")
