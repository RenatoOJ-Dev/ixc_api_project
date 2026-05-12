from handle__request import handle__request
from refactored import acess_direct_api__ex
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import streamlit as st

count = st_autorefresh(interval=5000, limit=None, key="fizzbuzzcounter")
st.title("Olá Técnico! 👋")
st.write(f"Count: {count}")
response__body__registros = handle__request()
df = pd.DataFrame(response__body__registros)
st.dataframe(df)

response__body__registros__ex = acess_direct_api__ex()
df2 = pd.DataFrame(response__body__registros__ex)
st.dataframe(df2)
