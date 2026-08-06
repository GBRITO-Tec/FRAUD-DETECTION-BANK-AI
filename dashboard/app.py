# dashboard/app.py
import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Dashboard de Monitoramento", layout="wide")

st.title("📊 Painel de Visualização & Predições ML")

st.sidebar.header("Navegação")
option = st.sidebar.selectbox("Selecione uma visão", ["Visão Geral", "Realizar Predição"])

if option == "Visão Geral":
    st.header("Dados Processados")
    try:
        df = pd.read_csv("data/processed/data_cleaned.csv")
        st.dataframe(df.head(10))
        st.metric(label="Total de Registros", value=len(df))
    except Exception as e:
        st.warning("Base de dados não encontrada em 'data/processed/data_cleaned.csv'.")

elif option == "Realizar Predição":
    st.header("Interface de Predição em Tempo Real")
    inputs = st.text_input("Insira as features separadas por vírgula (ex: 5.1, 3.5, 1.4, 0.2):")
    
    if st.button("Enviar para API"):
        if inputs:
            try:
                feature_list = [float(x.strip()) for x in inputs.split(",")]
                response = requests.post("http://localhost:8000/predict", json={"features": feature_list})
                if response.status_code == 200:
                    result = response.json()["prediction"]
                    st.success(f"Resultado da Predição: {result}")
                else:
                    st.error("Erro na resposta da API.")
            except Exception as e:
                st.error(f"Erro ao processar dados: {e}")
