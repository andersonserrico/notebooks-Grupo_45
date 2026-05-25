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
    vegetais = st.selectbox("Frequência de vegetais", ["Raramente", "As vezes", "Sempre"])
    refeicoes = st.selectbox("Refeições/dia", ["1 refeicao", "2 refeicoes", "3 refeicoes", "4 ou mais"])
    agua = st.selectbox("Consumo de água", ["< 1 L/dia", "1-2 L/dia", "> 2 L/dia"])
with col3:
    ativ_fisica = st.selectbox("Atividade física", ["Nenhuma", "1-2 dias/sem", "3-4 dias/sem", "5+ dias/sem"])
    telas = st.selectbox("Tempo de tela", ["0-2 h/dia", "3-5 h/dia", "> 5 h/dia"])

if st.button("Realizar Previsão"):
    imc = round(peso / (altura ** 2), 2)
    dados = pd.DataFrame([{
        'Genero': genero, 'Idade': float(idade), 'Historico_Familiar': familia, 
        'Consumo_Vegetais': vegetais, 'Refeicoes_Dia': refeicoes, 'Consumo_Agua': agua, 
        'Frequencia_Ativ_Fisica': ativ_fisica, 'Tempo_Telas': telas, 'IMC': imc
    }])
    st.success(f"Diagnóstico: {model.predict(dados)[0]}")
