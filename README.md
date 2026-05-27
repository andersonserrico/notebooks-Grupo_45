<div align="center">
  <img src="https://raw.githubusercontent.com/maikej910-del/notebooks-Grupo_45/main/logo.jpeg" alt="Logo Grupo 45" width="250">
</div>

# 🏥 Sistema Preditivo: Diagnóstico de Peso Corporal

## Tech Challenge FIAP (Fase 4) - Grupo 45 | Machine Learning aplicado à Saúde

🔗 **Acesse a aplicação em produção:** [Clique aqui para abrir o Sistema](https://notebooks-grupo45-xngddkmfv7koeyvmubsqco.streamlit.app/)

---

## 📌 Visão Geral Executiva

Este projeto foi desenvolvido como parte do Tech Challenge da FIAP (Fase 4) com foco na construção de um pipeline de Machine Learning de ponta a ponta para apoio à tomada de decisão clínica.

A solução consiste em um modelo preditivo treinado para classificar o risco e a classe de peso de um paciente com base em variáveis demográficas, comportamentais, histórico familiar e dados físicos. O algoritmo foi empacotado e disponibilizado em produção por meio de uma aplicação web interativa construída com a framework Streamlit.

O objetivo estratégico da solução é mitigar a subjetividade em avaliações limítrofes, acelerar a triagem de pacientes e fornecer uma ferramenta baseada em dados para suporte diagnóstico qualificado.

---

## 🎯 Objetivo de Negócio

Desenvolver um sistema inteligente e de alta performance capaz de:

- Auxiliar profissionais de saúde na identificação precoce do nível de sobrepeso/obesidade de forma padronizada.
- Automatizar o cálculo de indicadores cruciais (como o IMC) e variáveis compostas de estilo de vida no backend.
- Apoiar estratégias preventivas e tratamentos personalizados.
- Transformar dados brutos de rotina e saúde em informação clínica acionável em tempo real.

---

## 🧠 Arquitetura da Solução

A solução foi arquitetada utilizando práticas sólidas de Engenharia de Dados e Ciência de Dados, dividida em duas camadas principais:

### 1️⃣ Camada de Machine Learning (Modelagem)
- **Seleção de Features Estratégica:** Remoção intencional das variáveis brutas de "Peso" e "Altura" do conjunto de treino. Esta abordagem elimina o viés de multicolinearidade e força o algoritmo a avaliar o quadro clínico cruzando a proporção corporal (`IMC`) com as rotinas comportamentais do paciente.
- **Pipeline de Transformação:** Utilização de `ColumnTransformer` associado ao `RobustScaler` (para tratar dados numéricos com maior tolerância a discrepâncias) e `OneHotEncoder` (binarização categórica), mitigando completamente o risco de *Data Leakage*.
- **Algoritmo Preditivo:** Implementação de um modelo ensemble `RandomForestClassifier` com pesos balanceados (`class_weight='balanced'`) e restrições de profundidade para evitar o sobreajuste (overfitting).
- **Alta Performance:** O modelo calibrado atingiu uma **acurácia global de 94.64%** nos dados de validação.
- **Artefato Gerado:** O pipeline completo foi serializado no arquivo:
  `modelo_obesidade_rf.pkl`

### 2️⃣ Camada de Aplicação Web (Interface)
- Desenvolvida integralmente em **Streamlit** focando em usabilidade clínica e produtividade.
- **Entrada Nominativa:** Inclusão de campo para identificação do paciente, permitindo centralizar a consulta.
- **Interface Segura (Campos Vazios):** Todos os seletores e campos numéricos iniciam completamente limpos (`None` / `""`). Isso elimina valores padrões na tela e obriga o profissional de saúde a preencher cada informação de forma consciente, evitando diagnósticos acidentais.
- **Mapeamento Reverso no Backend:** Implementação de um dicionário de conversão oculto no código. O usuário seleciona opções textuais intuitivas na tela (ex: "Sempre", "Raramente"), e o sistema traduz automaticamente para os códigos numéricos exatos que o modelo exige.
- **Cálculo de Índices em Tempo Real:** Processamento automático das entradas com injeção instantânea do cálculo do IMC e do cálculo cruzado de score de atividade física.
- **Exportação de Relatórios:** Geração automatizada de relatórios em formato Excel (`.xlsx`) contendo os dados coletados do paciente e o respectivo diagnóstico clínico, facilitando o arquivamento ou a impressão dos resultados.

---

## 📊 Diagnóstico Analítico e Inteligência de Negócio

Esta seção consolida os principais cruzamentos de dados dinâmicos avaliados pelo algoritmo, indo além da leitura isolada de variáveis para entender a sinergia dos fatores de risco.

### Tema A: Perfil Demográfico e Dinâmica do IMC
- **Distribuição Populacional:** A base exibe uma forte concentração em Jovens Adultos (93.3%), seguidos por uma participação residual de Adolescentes (2.9%). Isto caracteriza um dataset focado majoritariamente em indivíduos em idade produtiva.
- **Linha de Tendência:** A análise epidemiológica confirma um avanço progressivo do Índice de Massa Corporal (IMC) médio à medida que o ciclo biológico do paciente avança, registrando saltos visíveis nas transições de faixa etária e atingindo a média crítica em idosos.
- **Assimetria de Gênero:** O mapeamento aponta desvios críticos nas faixas de risco elevado. Homens representam a maioria esmagadora da classe de Sobrepeso II, enquanto os quadros graves de Obesidade Tipo III (grau mais severo da patologia) têm associação estatística quase exclusiva com o gênero feminino.

### Tema B: Matriz Comportamental e Hábitos Nutricionais
- **Padrão de Fracionamento:** O volume diário de alimentação aponta que a maioria dos pacientes (58.7%) realiza o padrão de 3 refeições por dia. Isso indica que a desregulação do peso está atrelada à densidade calórica e à qualidade nutricional da rotina, e não necessariamente ao número de pausas alimentares.
- **Consumo de Fibras:** Registra-se um comportamento irregular em relação à ingestão de micronutrientes, com a maior fatia da amostra total (81.0%) admitindo o consumo de vegetais apenas de forma ocasional ("Às vezes").
- **Efeito Sinergico de Risco:** O cruzamento multivariado prova que pacientes que unem o consumo frequente de alimentos altamente calóricos ao hábito de lanchar "Sempre" entre as refeições principais sofrem um impacto devastador, elevando o IMC para os patamares mais severos da base.

### Tema C: Estilo de Vida e Fatores de Risco Combinados
- **Sedentarismo Estrutural:** A inatividade física atua de forma alarmante no dataset, visto que 56.4% da base reporta padrões de sedentarismo ("Nenhuma") ou rotina muito baixa (apenas 1 a 2 dias por semana).
- **Sensibilidade da Feature Composta:** O indicador unificado *Score_Atividade* (Frequência x Tempo) exibe alta capacidade discriminatória para o algoritmo. O indicador cai de forma abrupta de 1.15 nos pacientes em Peso Normal para apenas 0.05 no grupo com Obesidade Tipo III.
- **Carga Genética Hereditária:** A influência genética configura-se como um dos maiores fatores de risco transversais mapeados. Exatamente 100% de todos os indivíduos diagnosticados com Obesidade Tipo III possuem histórico familiar direto de sobrepeso.
- **Gatilho Metabólico:** A taxa de ingestão regular de álcool tem seu pico na faixa etária dos Jovens Adultos (4.9%), funcionando como um catalisador calórico inicial antes da desregulação metabólica crônica da meia-idade.

---

## 👤 Segmentação Estratégica por Personas Clínicas

Com base nos padrões comportamentais identificados nas árvores de decisão do modelo, consolidamos a base de dados em **3 Personas Clínicas de Risco** para direcionamento de intervenções preventivas hospitalares:

1. **Persona 1 - O Jovem Adulto Sedentário (Risco de Transição):** Paciente entre 18 e 35 anos, com histórico de consumo de álcool frequente e baixo escore de atividade física (0 a 1 dia/semana). Utiliza alimentos rápidos de alta caloria como compensação da rotina. Atualmente classificado em Sobrepeso II ou Obesidade I, apresentando a maior probabilidade de progressão de gravidade clínica nos próximos 5 anos.
2. **Persona 2 - A Paciente com Predisposição Genética Crônica:** Paciente do sexo feminino com coocorrência de histórico familiar positivo para obesidade em 100% dos casos. Apresenta metabolismo vulnerável à desregulação calórica rápida, estando correlacionada diretamente à Obesidade Tipo III. Exige abordagens terapêuticas intensivas devido à alta barreira genética.
3. **Persona 3 - O Paciente Hiperfracionador Calórico:** Paciente que realiza 4 ou mais refeições diárias e mantém o hábito de lanchar constantemente entre as pausas. Embora declare comer vegetais "Às vezes", o alto consumo calórico combinado atua em sinergia disparando o IMC médio para patamares graves, concentrando-se na Obesidade Tipo II.

---

## 📈 Diretrizes Clínicas e Recomendações Hospitalares

- **Protocolo de Triagem Automatizado com IA:** Integrar este sistema preditivo (`app.py`) logo na recepção do hospital ou ambulatório de especialidades. Ao capturar dados simples de hábitos de vida e calcular o IMC no backend, o hospital reduz o tempo de triagem clínica e encaminha o paciente de risco preventivo ao especialista em milissegundos.
- **Campanhas de Intervenção Precoce Focalizada:** Visto que o salto crítico do IMC médio ocorre na transição de Jovem Adulto para a Meia Idade, o hospital deve focar programas de medicina preventiva direcionados à faixa dos 18 aos 35 anos, atuando na conscientização da sinergia destrutiva entre sedentarismo e abuso calórico antes que o quadro se agrave.
- **Plano de Linha de Cuidado Personalizado por Persona:** Utilizar a classificação do modelo para segmentar o atendimento. As Personas 1 e 3 devem ser direcionadas a programas focados em reeducação de hábitos alimentares e ganho de score de atividade física. Já a Persona 2 deve receber suporte de alta complexidade (genética/endocrinologia) desde o primeiro dia de admissão clínica.

---

## 📂 Estrutura do Repositório

    notebooks-grupo_45/
    │
    ├── Tech_Fase_4_Grupo_45.ipynb   # Notebook principal com EDA, ETL e Treinamento
    ├── app.py                       # Código-fonte da aplicação web (Streamlit)
    ├── modelo_obesidade_rf.pkl      # Modelo de ML treinado e serializado
    ├── requirements.txt             # Dependências e versões exatas para o deploy
    ├── Obesity.csv                  # Base de dados bruta utilizada na ingestão
    ├── log.jpeg                     # Logotipo oficial do projeto
    └── obesity_tratada_grupo45.csv  # Base consolidada exportada para consumo em Data Viz

---

## 🛠️ Stack Tecnológica

- **Linguagem:** Python 3.10+
- **Manipulação de Dados:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn
- **Serialização:** Joblib
- **Desenvolvimento Web:** Streamlit
- **Geração de Relatórios:** XlsxWriter (Exportação para Excel)
- **Visualização de Dados:** Matplotlib, Seaborn
- **Controle de Versão:** Git & GitHub

---

## 🚀 Deploy e Produção

A aplicação encontra-se publicada na nuvem através do **Streamlit Community Cloud**, com um fluxo de deploy contínuo (CI/CD) conectado diretamente à branch `main` deste repositório.

**Link de Acesso:** [https://notebooks-grupo45-xngddkmfv7koeyvmubsqco.streamlit.app/](https://notebooks-grupo45-xngddkmfv7koeyvmubsqco.streamlit.app/)

**Diferenciais da Infraestrutura:**
- **Sincronização de Versões:** O arquivo `requirements.txt` trava as versões exatas de todas as bibliotecas (incluindo o motor gráfico e o gerador de planilhas), eliminando incompatibilidades do modelo em produção.
- **Inferências em Milissegundos:** O modelo de *Random Forest* permanece residente na memória do servidor, garantindo respostas imediatas assim que o formulário é validado.

---

## 📊 Impacto Estratégico

Esta solução comprova a viabilidade da aplicação prática de Ciência de Dados no cotidiano corporativo e hospitalar, garantindo:

- **Escalabilidade:** Uma ferramenta web leve que elimina a necessidade de softwares locais ou instalações pesadas.
- **Confiabilidade:** Padronização do diagnóstico através de um algoritmo robusto contra variabilidade clínica humana.
- **Eficiência:** Redução drástica do esforço manual em cálculos de triagem nutricional e geração de relatórios de avaliação.
