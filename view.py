# view.py

from qtd_os_exec.exe_os_get import fetch_os_em_execucao
from renato_all_os.engine_request import get_os_renato
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import streamlit as st
import redis
import json
import sys
import os

# fmt: off
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
# fmt: on


CACHE_KEY_OS_ABERTAS = "cache:os_abertas_por_tecnico"
CACHE_KEY_OS_FINALIZADAS = "cache:os_finalizadas_hoje"

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)


def get_cache(key: str) -> list:
    """Lê uma chave do Redis e retorna lista, ou vazia se não existir."""
    data = redis_client.get(key)
    return json.loads(data) if data else []


def dashboard_realtime():
    st_autorefresh(interval=10000, limit=None, key="dashboard_refresh")

    st.title("Olá Técnico! 👋")

    with st.container(border=True):
        st.subheader("BAIXA DO TÉCNICO :blue[RENATO]")
        os_renato = get_os_renato()
        st.dataframe(pd.DataFrame(os_renato))

    with st.container(border=True):
        st.subheader("ORDENS DE SERVIÇO EM :violet[EXECUÇÃO]")
        os_execucao = fetch_os_em_execucao()
        st.dataframe(pd.DataFrame(os_execucao))

    with st.container(border=True):
        st.subheader("QUANTIDADE DE OS POR :green[TÉCNICO]")
        st.dataframe(pd.DataFrame(get_cache(CACHE_KEY_OS_ABERTAS)))

    with st.container(border=True):
        st.subheader("QUANTIDADE DE OS FINALIZADA POR :yellow[TÉCNICO]")
        st.dataframe(pd.DataFrame(get_cache(CACHE_KEY_OS_FINALIZADAS)))


def renan_gomes():
    with st.container(border=True):
        st.subheader("Renan Gomes")
        st.dataframe()


pages = {
    "Dashboard Real Time": [
        st.Page(dashboard_realtime, title="Dashboard", icon="📊")
    ],
    "Dashboard For Tecnico": [
        st.Page('pages/renan_gomes.py', title='Renan Gomes', icon='👨')
    ]
}

pg = st.navigation(pages, position="top")
pg.run()
