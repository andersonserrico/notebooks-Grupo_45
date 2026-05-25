import streamlit as st
import joblib
import pandas as pd
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
    imc = round(peso / (altura ** 2), 2)
    # A ORDEM E OS NOMES DEVEM SER IDÊNTICOS AO df_modelo
    dados = pd.DataFrame([{
        'Genero': genero, 'Idade': float(idade), 'Historico_Familiar': familia,
        'Consumo_Alta_Caloria': calorico, 'Consumo_Vegetais': vegetais, 'Refeicoes_Dia': refeicoes,
        'Consumo_Entre_Refeicoes': lanches, 'Fumante': fumante, 'Consumo_Agua': agua,
        'Monitora_Calorias': monitora_cal, 'Frequencia_Ativ_Fisica': ativ_fisica,
        'Tempo_Exercicio': telas, 'Consumo_Alcool': alcool, 'Meio_Transporte': transporte,
        'IMC': imc, 'Score_Atividade': 0.0
    }])
    st.success(f"Diagnóstico: {model.predict(dados)[0]}")
