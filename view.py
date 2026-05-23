# view.py
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import streamlit as st
import redis
import json
import logging
from dotenv import load_dotenv
import os


load_dotenv()

redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')


CACHE_KEY_OS_ABERTAS = "cache:os_abertas_por_tecnico"
CACHE_KEY_OS_FINALIZADAS = "cache:os_finalizadas_hoje"
CACHE_KEY_OS_RENATO = "cache:os_baixa_renato"
CACHE_KEY_OS_EXECUCAO = "cache:os_em_execucao"

redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


def get_cache(key: str) -> list:
    """Lê uma chave do Redis e retorna lista, ou vazia se não existir."""
    try:
        data = redis_client.get(key)
        return json.loads(data) if data else []

    except Exception as e:
        logging.error(f'Erro ao acesso o Redis:{e}')
        return []


def dashboard_realtime():
    st_autorefresh(interval=10000, limit=None, key="dashboard_refresh")

    st.title("Olá Técnico! 👋")

    with st.container(border=True):
        st.subheader("BAIXA DO TÉCNICO :blue[RENATO]")
        st.dataframe(pd.DataFrame(get_cache(CACHE_KEY_OS_RENATO)))

    with st.container(border=True):
        st.subheader("ORDENS DE SERVIÇO EM :violet[EXECUÇÃO]")
        st.dataframe(pd.DataFrame(get_cache(CACHE_KEY_OS_EXECUCAO)))

    with st.container(border=True):
        st.subheader("QUANTIDADE DE OS POR :green[TÉCNICO]")
        st.dataframe(pd.DataFrame(get_cache(CACHE_KEY_OS_ABERTAS)))

    with st.container(border=True):
        st.subheader("QUANTIDADE DE OS FINALIZADA POR :yellow[TÉCNICO]")
        st.dataframe(pd.DataFrame(get_cache(CACHE_KEY_OS_FINALIZADAS)))


pages = {
    "Dashboard Real Time": [
        st.Page(dashboard_realtime, title="Dashboard", icon="📊")
    ]
}

pg = st.navigation(pages, position="top")
pg.run()
