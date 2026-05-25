import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Diagnóstico de Peso Corporal", page_icon="🩺", layout="wide")
st.title("🩺 Diagnóstico de Peso Corporal")

@st.cache_resource
def load_model():
    return joblib.load('modelo_obesidade_rf.pkl')

model = load_model()

st.subheader("Preencha os dados do paciente:")

col1, col2, col3 = st.columns(3)

with col1:
    genero = st.selectbox("Gênero", ["Masculino", "Feminino"])
    idade = st.number_input("Idade", min_value=1, max_value=100, value=25)
    altura = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, value=1.70, step=0.01)
    peso = st.number_input("Peso (kg)", min_value=10.0, max_value=250.0, value=70.0, step=0.1)
    familia = st.selectbox("Histórico Familiar de Obesidade?", ["Sim", "Nao"])
    fumante = st.selectbox("Fumante?", ["Sim", "Nao"])

with col2:
    calorico = st.selectbox("Consumo frequente de alimentos muito calóricos?", ["Sim", "Nao"])
    vegetais = st.selectbox("Frequência de consumo de vegetais", ["Raramente", "As vezes", "Sempre"])
    refeicoes = st.selectbox("Número de refeições principais por dia", ["1 refeicao", "2 refeicoes", "3 refeicoes", "4 ou mais"])
    lanches = st.selectbox("Consumo de lanches (entre refeições)", ["Nao", "As vezes", "Frequentemente", "Sempre"])
    agua = st.selectbox("Consumo diário de água", ["< 1 L/dia", "1-2 L/dia", "> 2 L/dia"])

with col3:
    monitora_cal = st.selectbox("Monitora ingestão calórica?", ["Sim", "Nao"])
    ativ_fisica = st.selectbox("Atividade física semanal", ["Nenhuma", "1-2 dias/sem", "3-4 dias/sem", "5+ dias/sem"])
    telas = st.selectbox("Tempo diário de tela", ["0-2 h/dia", "3-5 h/dia", "> 5 h/dia"])
    alcool = st.selectbox("Consumo de álcool", ["Nao", "As vezes", "Frequentemente", "Sempre"])
    transporte = st.selectbox("Transporte habitual", ["Carro", "Moto", "Bicicleta", "Transporte Publico", "A pe"])

st.markdown("---")

if st.button("Realizar Previsão"):
    # 1. Cálculo do IMC (Única feature calculada no backend agora)
    imc = round(peso / (altura ** 2), 2)

    # 2. Montagem do dicionário repassando os textos puros (O modelo vai entender!)
    dados_entrada = {
        'Genero': genero, 
        'Idade': float(idade), 
        'Altura': float(altura), 
        'Peso': float(peso),
        'Historico_Familiar': familia, 
        'Consumo_Alta_Caloria': calorico,
        'Consumo_Vegetais': vegetais, 
        'Refeicoes_Dia': refeicoes,
        'Consumo_Entre_Refeicoes': lanches, 
        'Fumante': fumante,
        'Consumo_Agua': agua, 
        'Monitora_Calorias': monitora_cal,
        'Frequencia_Ativ_Fisica': ativ_fisica, 
        'Tempo_Telas': telas,
        'Consumo_Alcool': alcool, 
        'Meio_Transporte': transporte, 
        'IMC': imc
    }

    df_input = pd.DataFrame([dados_entrada])

    try:
        resultado = model.predict(df_input)[0]
        st.success(f"**Resultado do Diagnóstico:** {resultado}")
    except Exception as e:
        st.error(f"Erro ao processar a predição: {e}")
