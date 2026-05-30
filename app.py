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
    # 1. Mapas de conversão (Frontend visual -> Backend numérico esperado pelo df_modelo)
    mapa_vegetais = {"Raramente": 1.0, "As vezes": 2.0, "Sempre": 3.0}
    mapa_refeicoes = {"1 refeicao": 1.0, "2 refeicoes": 2.0, "3 refeicoes": 3.0, "4 ou mais": 4.0}
    mapa_agua = {"< 1 L/dia": 1.0, "1-2 L/dia": 2.0, "> 2 L/dia": 3.0}
    mapa_ativ_fisica = {"Nenhuma": 0.0, "1-2 dias/sem": 1.0, "3-4 dias/sem": 2.0, "5+ dias/sem": 3.0}
    mapa_telas = {"0-2 h/dia": 0.0, "3-5 h/dia": 1.0, "> 5 h/dia": 2.0}

    # 2. Cálculos das Features de Engenharia
    imc = round(peso / (altura ** 2), 2)
    score_atividade = mapa_ativ_fisica[ativ_fisica] * mapa_telas[telas]

    # 3. Montagem do dicionário repassando os números
    dados_entrada = {
        'Genero': genero,
        'Idade': float(idade),
        'Altura': float(altura),
        'Peso': float(peso),
        'Historico_Familiar': familia,
        'Consumo_Alta_Caloria': calorico,
        'Consumo_Vegetais': mapa_vegetais[vegetais],
        'Refeicoes_Dia': mapa_refeicoes[refeicoes],
        'Consumo_Entre_Refeicoes': lanches,
        'Fumante': fumante,
        'Consumo_Agua': mapa_agua[agua],
        'Monitora_Calorias': monitora_cal,
        'Frequencia_Ativ_Fisica': mapa_ativ_fisica[ativ_fisica],
        'Tempo_Exercicio': mapa_telas[telas],
        'Consumo_Alcool': alcool,
        'Meio_Transporte': transporte,
        'IMC': imc,
        'Score_Atividade': score_atividade
    }

    df_input = pd.DataFrame([dados_entrada])

    try:
        resultado = model.predict(df_input)[0]
        st.success(f"**Resultado do Diagnóstico:** {resultado}")
    except Exception as e:
        st.error(f"Erro ao processar a predição: {e}")
