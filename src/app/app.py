import streamlit as st
import pandas as pd
import joblib
import json
from typing import Tuple, Dict

st.set_page_config(
    page_title="Previsão de Risco de Crédito",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

MODEL_DIR = "../models"
MODELOS = {
    "Regressão Logística": "logistic",
    "Random Forest": "random_forest",
    "XGBoost": "xgboost",
    "LightGBM": "lightgbm"
}

OPCOES = {
    "Status": {
        "Crédito negativo": "A11",
        "Crédito entre 0 e 200 €": "A12",
        "Crédito acima de 200 €": "A13",
        "Sem conta bancária": "A14"
    },
    "CreditHistory": {
        "Sem histórico de crédito": "A30",
        "Todas dívidas quitadas": "A31",
        "Dívidas existentes quitadas": "A32",
        "Atrasos no passado": "A33",
        "Histórico crítico": "A34"
    },
    "Purpose": {
        "Carro novo": "A40",
        "Carro usado": "A41",
        "Móveis/equipamentos": "A42",
        "Eletrônicos (TV/rádio)": "A43",
        "Eletrodomésticos": "A44",
        "Reformas": "A45",
        "Educação": "A46",
        "Férias": "A48",
        "Negócios": "A49",
        "Outros": "A410"
    },
    "Savings": {
        "≥ 1000 €": "A61",
        "500 € a 1000 €": "A62",
        "100 € a 500 €": "A63",
        "< 100 €": "A64",
        "Sem informações": "A65"
    },
    "Employment": {
        "≥ 7 anos": "A71",
        "4 a 7 anos": "A72",
        "1 a 4 anos": "A73",
        "< 1 ano": "A74",
        "Desempregado": "A75"
    },
    "PersonalStatusSex": {
        "Homem solteiro": "A93",
        "Homem casado/divorciado": "A92",
        "Homem (outro)": "A91",
        "Mulher casada": "A95",
        "Mulher (outro)": "A94"
    },
    "OtherDebtors": {
        "Nenhum": "A101",
        "Co-devedor": "A102",
        "Fiador": "A103"
    },
    "Property": {
        "Imóvel": "A121",
        "Seguro de vida": "A122",
        "Automóvel": "A123",
        "Sem informações": "A124"
    },
    "OtherInstallmentPlans": {
        "Banco": "A141",
        "Lojas": "A142",
        "Nenhum": "A143"
    },
    "Housing": {
        "Alugada": "A151",
        "Própria": "A152",
        "Gratuita": "A153"
    },
    "Job": {
        "Desempregado": "A171",
        "Não qualificado": "A172",
        "Qualificado": "A173",
        "Altamente qualificado": "A174"
    },
    "Telephone": {
        "Sem telefone": "A191",
        "Com telefone": "A192"
    },
    "ForeignWorker": {
        "Sim": "A201",
        "Não": "A202"
    }
}

def local_css():
    st.markdown("""
    <style>
        /* Estilos gerais */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #222266; /* Cor do texto alterada */
        }

        /* Cabeçalho */
        .header {
            background-color: #4a6fa5;
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }

        .header h1 {
            margin: 0;
            font-size: 2rem;
        }

        .header p {
            margin: 0;
            opacity: 0.9;
        }

        /* Métricas */
        .stMetric {
            border-left: 4px solid #4a6fa5;
            padding-left: 1rem;
            margin-bottom: 1rem;
        }

        /* Caixas de resultado */
        .result-box {
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        }

        .good-result {
            background-color: #e6f7e6;
            border-left: 5px solid #2ecc71;
            padding: 1rem;
            border-radius: 5px;
            color: #226622; /* Cor do texto alterada para resultado bom */
        }

        .bad-result {
            background-color: #ffebee;
            border-left: 5px solid #e74c3c;
            padding: 1rem;
            border-radius: 5px;
            color: #a80000; /* Cor do texto alterada para resultado ruim */
        }

        /* Botões */
        .stButton>button {
            background-color: #4a6fa5;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            transition: all 0.3s;
        }

        .stButton>button:hover {
            background-color: #3a5a80;
            transform: translateY(-2px);
        }

        /* Formulário */
        .stSelectbox, .stSlider, .stNumberInput {
            margin-bottom: 1rem;
        }

        /* Responsividade */
        @media (max-width: 768px) {
            .header h1 {
                font-size: 1.5rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

def carregar_modelo(nome_modelo: str) -> Tuple[object, Dict]:
    try:
        modelo = joblib.load(f"{MODEL_DIR}/{nome_modelo}_model.pkl")
        with open(f"{MODEL_DIR}/{nome_modelo}_metrics.json", "r") as f:
            metricas = json.load(f)
        return modelo, metricas
    except Exception as e:
        st.error(f"Erro ao carregar modelo: {str(e)}")
        return None, {}

def mostrar_metricas(metricas: Dict) -> None:
    st.subheader("📊 Desempenho do Modelo")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Acurácia", f"{metricas['metrics'].get('accuracy', 0):.2%}")
        st.metric("Precisão", f"{metricas['metrics'].get('precision', 0):.2%}")
    
    with col2:
        st.metric("Recall", f"{metricas['metrics'].get('recall', 0):.2%}")
        st.metric("F1-Score", f"{metricas['metrics'].get('f1', 0):.2%}")
    
    with col3:
        st.metric("AUC-ROC", f"{metricas['metrics'].get('roc_auc', 0):.2%}")
        st.metric("Precisão Média", f"{metricas['metrics'].get('average_precision', 0):.2%}")

def montar_formulario() -> pd.DataFrame:
    st.subheader("📝 Informações do Cliente")
    
    col1, col2 = st.columns(2)
    
    dados = {}
    
    with col1:
        dados["Status"] = st.selectbox("Situação da Conta", list(OPCOES["Status"].keys()))
        dados["CreditHistory"] = st.selectbox("Histórico de Crédito", list(OPCOES["CreditHistory"].keys()))
        dados["Purpose"] = st.selectbox("Propósito do Empréstimo", list(OPCOES["Purpose"].keys()))
        dados["Savings"] = st.selectbox("Reservas Financeiras", list(OPCOES["Savings"].keys()))
        dados["Employment"] = st.selectbox("Tempo de Emprego", list(OPCOES["Employment"].keys()))
        dados["PersonalStatusSex"] = st.selectbox("Estado Civil/Gênero", list(OPCOES["PersonalStatusSex"].keys()))
        dados["OtherDebtors"] = st.selectbox("Outros Devedores", list(OPCOES["OtherDebtors"].keys()))
    
    with col2:
        dados["Property"] = st.selectbox("Propriedades", list(OPCOES["Property"].keys()))
        dados["OtherInstallmentPlans"] = st.selectbox("Outros Planos de Pagamento", list(OPCOES["OtherInstallmentPlans"].keys()))
        dados["Housing"] = st.selectbox("Situação Habitacional", list(OPCOES["Housing"].keys()))
        dados["Job"] = st.selectbox("Ocupação Profissional", list(OPCOES["Job"].keys()))
        dados["Telephone"] = st.selectbox("Telefone", list(OPCOES["Telephone"].keys()))
        dados["ForeignWorker"] = st.selectbox("Trabalhador Estrangeiro", list(OPCOES["ForeignWorker"].keys()))

    st.subheader("🔢 Dados Numéricos")
    num_col1, num_col2, num_col3 = st.columns(3)
    
    with num_col1:
        dados["Duration"] = st.slider("Duração (meses)", 4, 72, 24, help="Duração do crédito em meses")
        dados["CreditAmount"] = st.slider("Valor do Crédito (€)", 250, 20000, 5000, step=100)
    
    with num_col2:
        dados["InstallmentRate"] = st.selectbox("Taxa de Parcela (%)", [1, 2, 3, 4])
        dados["ResidenceSince"] = st.selectbox("Tempo na Residência (anos)", [1, 2, 3, 4])
    
    with num_col3:
        dados["Age"] = st.slider("Idade", 18, 75, 35)
        dados["ExistingCredits"] = st.selectbox("Créditos Existentes", [1, 2, 3, 4])
        dados["NumPeopleLiable"] = st.selectbox("Dependentes", [1, 2])
    
    dados_convertidos = {}
    for campo, valor in dados.items():
        if campo in OPCOES:
            dados_convertidos[campo] = OPCOES[campo][valor]
        else:
            dados_convertidos[campo] = valor
    
    return pd.DataFrame([dados_convertidos])

def main():
    local_css()
    
    st.markdown("""
    <div class="header">
        <h1>💰 Análise de Risco de Crédito</h1>
    </div>
    """, unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown("### Configurações")
        modelo_nome_ui = st.selectbox("Selecione o Modelo", list(MODELOS.keys()), 
                                    help="Escolha o algoritmo de machine learning para análise")
        st.markdown("---")
        st.markdown("""
        **Como usar:**
        1. Selecione o modelo
        2. Preencha os dados do cliente
        3. Clique em 'Prever Risco'
        """)
    
    modelo_interno = MODELOS[modelo_nome_ui]
    modelo, metricas = carregar_modelo(modelo_interno)
    
    if modelo:
        mostrar_metricas(metricas)
        df_input = montar_formulario()
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔮 Prever Risco", use_container_width=True):
                with st.spinner("Analisando risco..."):
                    try:
                        pred = modelo.predict(df_input)[0]
                        prob = modelo.predict_proba(df_input)[0][1]
                        
                        if pred == 1:
                            st.markdown(f"""
                            <div class='bad-result'>
                                <h2>🔴 Risco Alto</h2>
                                <p>Probabilidade de inadimplência: {prob:.2%}</p>
                                <p>Recomendação: Análise manual recomendada</p>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                            <div class='good-result'>
                                <h2>🟢 Risco Baixo</h2>
                                <p>Probabilidade de inadimplência: {prob:.2%}</p>
                                <p>Recomendação: Crédito pode ser aprovado</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Mostrar detalhes da análise
                        with st.expander("📈 Detalhes da Análise"):
                            st.write("**Fatores mais relevantes:**")
                            st.write("- Histórico de crédito")
                            st.write("- Valor do empréstimo")
                            st.write("- Situação de emprego")
                            
                            st.write("**Dados enviados para análise:**")
                            st.dataframe(df_input.style.highlight_max(axis=0))
                    
                    except Exception as e:
                        st.error(f"Erro na análise: {str(e)}")

if __name__ == "__main__":
    main()