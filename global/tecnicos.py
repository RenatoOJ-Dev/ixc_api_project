# global/tecnicos.py

TECNICOS: dict[int, str] = {
    89: "Renan Gomes",
    260: "Gobbo",
    # 43:  "Michel",   # comentado
    # 87:  "Saulo",    # comentado
    180: "Danilo",
    181: "Eder",
    248: "Jhon",
    270: "Kevin",
    220: "Dalmo",
    294: "Rodrigo",
    264: "Renato",
}


def get_nome_tecnico(id_tecnico) -> str:
    return TECNICOS.get(int(id_tecnico), f"Técnico #{id_tecnico}")
