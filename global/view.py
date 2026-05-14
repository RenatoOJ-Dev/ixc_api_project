from handle__request import handle__request
from refactored import acess_direct_api__ex
from streamlit_autorefresh import st_autorefresh
from src.app_os_po_tec import tec_total
import pandas as pd
import streamlit as st

count = st_autorefresh(interval=10000, limit=None, key="fizzbuzzcounter")
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
response__body__registros__all = tec_total()
df2 = pd.DataFrame(response__body__registros__all)
st.dataframe(df2)
