from engine__request import acess_direct_api
from dotenv import load_dotenv
import os


load_dotenv()


def handle__request() -> list | None:
    dict__api = acess_direct_api()
    total__registros = dict__api.get('total', 0)
    body__registros = dict__api.get('registros', None)

    response__body__resgistros = subfun__interable__body__registros(body__registros=body__registros)
    if response__body__resgistros:
        return response__body__resgistros
    return None


def subfun__interable__body__registros(body__registros: list) -> list | None:
    if body__registros:
        list_response_body_registros = [{
            'bairro': registros.get('bairro', 'null'),
            'status': registros.get('status', 'null'),
            'mensagem': registros.get('mensagem', 'null')
        }for registros in body__registros]
        return list_response_body_registros
    return None
