def surface_area_of_cube(edge_length: float) -> str:
    return f'A area superficial de um cubo é {6 * edge_length ** 2}'


def congratulations(name: str) -> str:
    return f'Bem vindo {name}'


type Vector = list[float]
def scale(scalar: float, vector: Vector) -> Vector:
