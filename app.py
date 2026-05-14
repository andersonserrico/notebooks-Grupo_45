
import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Diagnóstico de Obesidade", page_icon="🩺")
st.title("🩺 Sistema Preditivo: Diagnóstico de Obesidade")

@st.cache_resource
def load_model():
    return joblib.load('modelo_obesidade_rf.pkl')

model = load_model()

st.sidebar.header("Perfil do Paciente")
col1, col2 = st.columns(2)

with col1:
    genero = st.selectbox("Gênero", ["Male", "Female"])
    idade = st.number_input("Idade", min_value=1, max_value=100, value=25)
    altura = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, value=1.70, step=0.01)
    peso = st.number_input("Peso (kg)", min_value=10.0, max_value=250.0, value=70.0, step=0.1)

with col2:
    familia = st.selectbox("Histórico Familiar de Sobrepeso?", ["yes", "no"])
    calorico = st.selectbox("Consome alimentos calóricos frequentemente?", ["yes", "no"])
    agua = st.slider("Consumo diário de água (1 a 3)", 1, 3, 2)
    vegetais = st.slider("Frequência de consumo de vegetais (1 a 3)", 1, 3, 2)

dados_entrada = {
    'Gender': genero, 'Age': idade, 'Height': altura, 'Weight': peso,
    'family_history': familia, 'FAVC': calorico, 'FCVC': vegetais, 'CH2O': agua
}

if st.button("Executar Predição de Risco"):
    df_input = pd.DataFrame([dados_entrada])
    resultado = model.predict(df_input)[0]
    st.subheader(f"Resultado: {resultado}")
