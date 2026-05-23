NOMES_TECNICOS = [
    "RENAN GOMES",
    "GOBBO",
    "DANILO",
    "EDER",
    "JHON",
    "KEVIN",
    "RODRIGO",
]

TECNICOS: dict[int, str] = {
    89: "Renan Gomes",
    260: "Gobbo",
    180: "Danilo",
    181: "Eder",
    248: "Jhon",
    270: "Kevin",
    294: "Rodrigo",
    264: "Renato",
}


def get_nome_tecnico(id_tecnico) -> str:
    try:
        return TECNICOS.get(int(id_tecnico), f"Técnico #{id_tecnico}")
    except (ValueError, TypeError):
        return f"Técnico #{id_tecnico}"
