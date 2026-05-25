import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Diagnóstico de Peso", layout="wide")
st.title("🩺 Diagnóstico de Peso Corporal")
model = joblib.load('modelo_obesidade_rf.pkl')

col1, col2, col3 = st.columns(3)
with col1:
    genero = st.selectbox("Gênero", ["Masculino", "Feminino"])
    idade = st.number_input("Idade", 1, 100, 25)
    altura = st.number_input("Altura (m)", 1.0, 2.5, 1.70, 0.01)
    peso = st.number_input("Peso (kg)", 10.0, 250.0, 70.0, 0.1)
    familia = st.selectbox("Histórico Familiar?", ["Sim", "Nao"])
with col2:
    calorico = st.selectbox("Consumo de alimentos calóricos?", ["Sim", "Nao"])
    vegetais = st.selectbox("Frequência de vegetais", ["Raramente", "As vezes", "Sempre"])
    refeicoes = st.selectbox("Refeições/dia", ["1 refeicao", "2 refeicoes", "3 refeicoes", "4 ou mais"])
    lanches = st.selectbox("Consumo de lanches", ["Nao", "As vezes", "Frequentemente", "Sempre"])
    agua = st.selectbox("Consumo de água", ["< 1 L/dia", "1-2 L/dia", "> 2 L/dia"])
with col3:
    fumante = st.selectbox("Fumante?", ["Sim", "Nao"])
    monitora_cal = st.selectbox("Monitora ingestão calórica?", ["Sim", "Nao"])
    ativ_fisica = st.selectbox("Atividade física", ["Nenhuma", "1-2 dias/sem", "3-4 dias/sem", "5+ dias/sem"])
    telas = st.selectbox("Tempo de tela", ["0-2 h/dia", "3-5 h/dia", "> 5 h/dia"])
    alcool = st.selectbox("Consumo de álcool", ["Nao", "As vezes", "Frequentemente", "Sempre"])
    transporte = st.selectbox("Transporte habitual", ["Carro", "Moto", "Bicicleta", "Transporte Publico", "A pe"])

if st.button("Realizar Previsão"):
    # 1. Engenharia de Features e Cálculos
    imc = round(peso / (altura ** 2), 2)
    
    # 2. Mapeamento Reverso (Texto -> Número) baseado na análise exploratória
    vegetais_map = {"Raramente": 1, "As vezes": 2, "Sempre": 3}
    refeicoes_map = {"1 refeicao": 1, "2 refeicoes": 2, "3 refeicoes": 3, "4 ou mais": 4}
    agua_map = {"< 1 L/dia": 1, "1-2 L/dia": 2, "> 2 L/dia": 3}
    ativ_map = {"Nenhuma": 0, "1-2 dias/sem": 1, "3-4 dias/sem": 2, "5+ dias/sem": 3}
    tela_map = {"0-2 h/dia": 0, "3-5 h/dia": 1, "> 5 h/dia": 2}
    
    # Calculando score de atividade real
    score_atv = float(ativ_map[ativ_fisica] * tela_map[telas])

    # 3. Montagem do DataFrame com colunas e tipos exatos do treino
    dados = pd.DataFrame([{
        'Genero': genero, 
        'Idade': float(idade), 
        'Historico_Familiar': familia,
        'Consumo_Alta_Caloria': calorico, 
        'Consumo_Vegetais': vegetais_map[vegetais], 
        'Refeicoes_Dia': refeicoes_map[refeicoes],
        'Consumo_Entre_Refeicoes': lanches, 
        'Fumante': fumante, 
        'Consumo_Agua': agua_map[agua],
        'Monitora_Calorias': monitora_cal, 
        'Frequencia_Ativ_Fisica': ativ_map[ativ_fisica],
        'Tempo_Exercicio': tela_map[telas], 
        'Consumo_Alcool': alcool, 
        'Meio_Transporte': transporte,
        'IMC': float(imc), 
        'Score_Atividade': score_atv
    }])
    
    st.success(f"Diagnóstico Clínico AI: **{model.predict(dados)[0]}**")
