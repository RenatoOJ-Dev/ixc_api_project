from handle__request import handle__request
from refactored import acess_direct_api__ex
from streamlit_autorefresh import st_autorefresh
from src.app_os_po_tec import tec_total
import pandas as pd
import streamlit as st
import redis
import json


count = st_autorefresh(interval=10000, limit=None, key="fizzbuzzcounter")
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

st.title("Olá Técnico! 👋")
st.write(f"Count: {count}")
st.subheader("BAIXA DO TÉCNICO :blue[RENATO]")
response__body__registros = handle__request()
df = pd.DataFrame(response__body__registros)
st.dataframe(df)


st.subheader("ORDENS DE SERVIÇO EM :violet[EXECUÇÃO]")
response__body__registros__ex = acess_direct_api__ex()
df2 = pd.DataFrame(response__body__registros__ex)
st.dataframe(df2)

st.subheader("QUANTIDADE DE OS POR :green[TÉCNICO]")
cache = r.get("tec_total")
if cache:
    response__body__registros__all = json.loads(cache)
else:
    response__body__registros__all = []  # ainda não tem dado no cache

df3 = pd.DataFrame(response__body__registros__all)
st.dataframe(df3)
