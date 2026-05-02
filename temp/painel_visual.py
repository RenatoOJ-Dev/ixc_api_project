# painel_simples.py
# Versão Streamlit do seu código que já funciona

import streamlit as st
import requests
import json
import pandas as pd

# ===============================
# ⚙️ CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(page_title="OS por Técnico", layout="wide")
st.title("🔧 OS por Técnico - IXC")

# ===============================
# 🔐 SUAS CONFIGURAÇÕES (mantidas iguais)
# ===============================
url = "https://central.nv7.net.br/webservice/v1/su_oss_chamado"

headers = {
    'ixcsoft': 'listar',
    'Authorization': 'Basic MjgwOmNkNzgxN2JhN2M4ZjRjMWFmZWNmZDg4MmUwMWY5OTZlNGJkMDk0ZTM5NzAxNWVkMmY4MzQ5NzMwZWQ0ZTIxYmQ='
}

lista_de_tecnicos = [
    "renan gomes",
    "gobbo",
    "wesley",
    "michel",
    "saulo",
    "danilo",
    "eder",
    "jhon",
    "marcelo",
    "renato"
]

# ===============================
# 🔧 FUNÇÃO COM CACHE (para não consultar toda vez)
# ===============================


@st.cache_data(ttl=300)  # Cache por 5 minutos
def buscar_dados_tecnicos(lista_tecnicos):
    """
    Mantém EXATAMENTE a sua lógica, só coleta os dados em vez de printar
    """
    resultados = []  # ← Lista para guardar os dados

    for tec in lista_tecnicos:
        grid_param = [
            {
                "TB": "view_funcionarios_setor.funcionario",
                "OP": "L",
                "P": tec
            },
            {
                "TB": "su_oss_chamado.status",
                "OP": "IN",
                "P": "'A','DS','AN','EX','EN','AS','RAG','AG'"
            }
        ]

        grid_param_string = json.dumps(grid_param)

        payload = {
            'action': 'grid',
            'page': '1',
            'rp': '10',  # ← Aumentei de 1 para 20 para pegar mais OS
            'sortname': 'su_oss_chamado.id',
            'sortorder': 'desc',
            'grid_param': grid_param_string,
        }

        response = requests.post(url, headers=headers, data=payload)
        dados = response.json()
        registros = dados.get('registros', [])
        total = dados.get('total', 0)

        # Sua lógica original de extrair id_tecnico
        for id_tec in registros:
            id_atual_tec = id_tec.get('id_tecnico')

            # Em vez de print, adiciona na lista de resultados
            resultados.append({
                'Técnico Buscado': tec,
                'Total OS': total,
                'ID Técnico': id_atual_tec,
                'ID OS': id_tec.get('id'),
                'Status': id_tec.get('status')
            })

    return resultados


# ===============================
# 🎛️ INTERFACE (Sidebar e Botões)
# ===============================
st.sidebar.header("⚙️ Opções")

# Botão para forçar atualização (limpa o cache)
if st.sidebar.button("🔄 Atualizar Dados"):
    st.cache_data.clear()

# Barra de progresso enquanto carrega
with st.spinner('📡 Consultando IXC...'):
    dados_coletados = buscar_dados_tecnicos(lista_de_tecnicos)

# ===============================
# 📊 EXIBIR RESULTADOS
# ===============================
if dados_coletados:
    # Métrica simples
    total_geral = len(dados_coletados)
    st.metric("📋 Total de OS encontradas", total_geral)

    # Converter lista de dicts em DataFrame (tabela)
    df = pd.DataFrame(dados_coletados)

    # Agrupar para mostrar resumo por técnico
    st.subheader("📊 Resumo por Técnico")
    resumo = df.groupby(['Técnico Buscado', 'ID Técnico']).size().reset_index(name='Qtd OS')
    st.dataframe(resumo, use_container_width=True)

    # Tabela completa (opcional, pode esconder se quiser)
    with st.expander("🔍 Ver todas as OS individualmente"):
        st.dataframe(df, use_container_width=True)

else:
    st.warning("⚠️ Nenhuma OS encontrada ou erro na conexão.")

# Rodapé
st.caption("Dados consultados via API IXC | Atualiza a cada 5 minutos")
