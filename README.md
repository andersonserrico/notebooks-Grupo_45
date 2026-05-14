# 🏥 Sistema Preditivo: Diagnóstico de Peso Corporal

## Tech Challenge FIAP (Fase 4) - Grupo 45 | Machine Learning aplicado à Saúde

---

## 📌 Visão Geral Executiva

Este projeto foi desenvolvido como parte do Tech Challenge da FIAP (Fase 4) com foco na construção de um pipeline de Machine Learning de ponta a ponta para apoio à tomada de decisão clínica.

A solução consiste em um modelo preditivo treinado para classificar o risco e a classe de peso de um paciente com base em variáveis demográficas, comportamentais, histórico familiar e dados físicos. O algoritmo foi empacotado e disponibilizado em produção por meio de uma aplicação web interativa construída com a framework Streamlit.

O objetivo estratégico da solução é mitigar a subjetividade em avaliações limítrofes, acelerar a triagem de pacientes e fornecer uma ferramenta baseada em dados para suporte diagnóstico.

---

## 🎯 Objetivo de Negócio

Desenvolver um sistema inteligente e de alta performance capaz de:

- Auxiliar profissionais de saúde na identificação precoce do nível de sobrepeso/obesidade.
- Automatizar o cálculo de indicadores cruciais (como o IMC) no backend.
- Apoiar estratégias preventivas e tratamentos personalizados.
- Transformar dados brutos de saúde em informação acionável em tempo real.

---

## 🧠 Arquitetura da Solução

A solução foi arquitetada utilizando práticas sólidas de Engenharia de Dados e Ciência de Dados, dividida em duas camadas principais:

### 1️⃣ Camada de Machine Learning (Modelagem)
- **Sanitização e Engenharia de Features:** Tratamento de dados, tradução do dicionário de dados para o contexto local, remoção de ruídos decimais e criação de features de domínio (IMC).
- **Pipeline de Transformação:** Utilização de `ColumnTransformer` com `StandardScaler` (padronização numérica) e `OneHotEncoder` (binarização categórica mitigando *Data Leakage*).
- **Algoritmo Preditivo:** Implementação de um modelo ensemble `RandomForestClassifier` com pesos balanceados (`class_weight='balanced'`).
- **Alta Performance:** O modelo atingiu uma **acurácia global de 98.58%** nos dados de teste.
- **Artefato Gerado:** O pipeline completo foi serializado no arquivo:
  `modelo_obesidade_rf.pkl`

### 2️⃣ Camada de Aplicação Web (Interface)
- Desenvolvida integralmente em **Streamlit**.
- Interface interativa, responsiva e dividida em colunas estruturadas para otimizar o fluxo de preenchimento médico.
- Processamento automático das entradas com injeção do cálculo de IMC em tempo real no backend.
- Exibição instantânea do diagnóstico estimado pela Inteligência Artificial.
- Artefato principal da interface:
  `app.py`

---

## 📂 Estrutura do Repositório

    notebooks-grupo_45/
    │
    ├── Tech_Fase_4_Grupo_45.ipynb   # Notebook principal com EDA, ETL e Treinamento
    ├── app.py                       # Código-fonte da aplicação web (Streamlit)
    ├── modelo_obesidade_rf.pkl      # Modelo de ML treinado e serializado
    ├── requirements.txt             # Dependências e versões exatas para o deploy
    ├── Obesity.csv                  # Base de dados bruta utilizada na ingestão
    └── obesity_tratada_grupo45.csv  # Base consolidada exportada para consumo em Data Viz

---

## 🛠️ Stack Tecnológica

- **Linguagem:** Python 3.10+
- **Manipulação de Dados:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn
- **Serialização:** Joblib
- **Desenvolvimento Web:** Streamlit
- **Visualização de Dados:** Matplotlib, Seaborn
- **Controle de Versão:** Git & GitHub

---

## 🚀 Deploy e Produção

A aplicação encontra-se publicada na nuvem através do **Streamlit Community Cloud**, com um fluxo de deploy contínuo (CI/CD) conectado diretamente à branch `main` deste repositório.

**Diferenciais da Infraestrutura:**
- **Sincronização de Versões:** O arquivo `requirements.txt` trava as versões exatas das bibliotecas (Pandas, Scikit-learn, Joblib) usadas no treinamento, eliminando erros de descompactação do modelo em produção.
- **Cache de Memória:** Implementação do decorador `@st.cache_resource` para manter o modelo de *Random Forest* residente na memória do servidor, garantindo inferências em milissegundos.

---

## 📊 Impacto Estratégico

Esta solução comprova a viabilidade da aplicação prática de Inteligência Artificial no cotidiano hospitalar, garantindo:

- **Escalabilidade:** Uma ferramenta web leve que elimina a necessidade de softwares locais pesados.
- **Confiabilidade:** Padronização diagnóstica através de um algoritmo robusto contra variabilidade clínica.
- **Eficiência:** Redução drástica de esforço manual em cálculos de triagem nutricional.

O projeto evidencia a capacidade analítica do Grupo 45 em transformar dados complexos em um produto funcional, preditivo e pronto para o ambiente de saúde real.
