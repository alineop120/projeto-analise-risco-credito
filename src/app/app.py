import streamlit as st
import numpy as np
import joblib
from pydantic import BaseModel, field_validator
from typing import List, Literal
import numpy as np

class EntradaCliente(BaseModel):
    LIMIT_BAL: float
    SEX: Literal[1, 2]
    EDUCATION: Literal[1, 2, 3, 4]
    MARRIAGE: Literal[1, 2, 3]
    AGE: int
    PAY_0: int
    PAY_2: int
    PAY_3: int
    PAY_4: int
    PAY_5: int
    PAY_6: int
    BILL_AMT: List[float]
    PAY_AMT: List[float]

    @field_validator('BILL_AMT', 'PAY_AMT')
    @classmethod
    def validar_tamanho_lista(cls, v):
        if len(v) != 6:
            raise ValueError("As listas BILL_AMT e PAY_AMT devem ter exatamente 6 elementos.")
        return v

    def to_numpy(self):
        return np.array([
            self.LIMIT_BAL,
            self.SEX,
            self.EDUCATION,
            self.MARRIAGE,
            self.AGE,
            self.PAY_0, self.PAY_2, self.PAY_3,
            self.PAY_4, self.PAY_5, self.PAY_6,
            *self.BILL_AMT,
            *self.PAY_AMT
        ]).reshape(1, -1)

# --- STREAMLIT UI ---
st.set_page_config(page_title="Analisador de Crédito", layout="centered")
st.title("🔍 Previsão de Inadimplência")

st.markdown("Selecione o modelo de previsão:")
model_choice = st.selectbox(
    "Modelo",
    ["Modelo 001", "Modelo 002", "Modelo 003"],
    format_func=lambda x: x
)

# Carregar o modelo com base na escolha
model_path = {
    "Modelo 001": "./models/modelo_001.pkl",
    "Modelo 002": "./models/modelo_002.pkl",
    "Modelo 003": "./models/modelo_003.pkl"
}.get(model_choice, "./models/modelo_001.pkl")

model = joblib.load(model_path)

st.markdown("Insira os dados do cliente abaixo:")

with st.form("formulario_cliente"):
    col1, col2 = st.columns(2)

    with col1:
        LIMIT_BAL = st.number_input("Limite de Crédito", min_value=0.0, step=1000.0)
        SEX = st.selectbox("Sexo", [1, 2], format_func=lambda x: "Masculino" if x == 1 else "Feminino")
        EDUCATION = st.selectbox("Educação", [1, 2, 3, 4], format_func=lambda x: ["Pós", "Graduação", "Ensino Médio", "Outros"][x - 1])
        MARRIAGE = st.selectbox("Estado Civil", [1, 2, 3], format_func=lambda x: ["Casado", "Solteiro", "Outros"][x - 1])
        AGE = st.slider("Idade", 18, 100, 30)

    with col2:
        PAY_0 = st.slider("Atraso mês atual", -2, 10, 0)
        PAY_2 = st.slider("Atraso mês -1", -2, 10, 0)
        PAY_3 = st.slider("Atraso mês -2", -2, 10, 0)
        PAY_4 = st.slider("Atraso mês -3", -2, 10, 0)
        PAY_5 = st.slider("Atraso mês -4", -2, 10, 0)
        PAY_6 = st.slider("Atraso mês -5", -2, 10, 0)

    st.subheader("💳 Valores das Faturas (6 meses)")
    bill_amt = [st.number_input(f"Fatura mês -{i}", key=f"bill_{i}") for i in range(6)]

    st.subheader("💸 Pagamentos Efetuados (6 meses)")
    pay_amt = [st.number_input(f"Pagamento mês -{i}", key=f"pay_{i}") for i in range(6)]

    submit = st.form_submit_button("🔮 Prever Inadimplência")

if submit:
    try:
        entrada = EntradaCliente(
            LIMIT_BAL=LIMIT_BAL,
            SEX=SEX,
            EDUCATION=EDUCATION,
            MARRIAGE=MARRIAGE,
            AGE=AGE,
            PAY_0=PAY_0,
            PAY_2=PAY_2,
            PAY_3=PAY_3,
            PAY_4=PAY_4,
            PAY_5=PAY_5,
            PAY_6=PAY_6,
            BILL_AMT=bill_amt,
            PAY_AMT=pay_amt
        )

        entrada_np = entrada.to_numpy()
        pred = model.predict(entrada_np)[0]
        prob = model.predict_proba(entrada_np)[0][1]

        st.success("✅ Resultado: INADIMPLENTE" if pred == 1 else "✅ Resultado: ADIMPLENTE")
        st.info(f"Probabilidade de inadimplência: **{prob*100:.2f}%**")

    except Exception as e:
        st.error(f"Erro ao processar entrada: {str(e)}")