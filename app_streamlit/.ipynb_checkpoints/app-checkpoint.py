import streamlit as st
import pandas as pd
import joblib

st.title("Análise de Risco de Crédito")

# Carrega modelo e escalonador
modelo = joblib.load('../resultados/modelos/modelo_rf.pkl')
colunas = joblib.load('../resultados/modelos/colunas_treinamento.pkl')  # Deve conter os 23 nomes

# Inputs do usuário
limite = st.number_input('Limite de Crédito', min_value=0, value=20000)
sexo = st.selectbox('Sexo', options=[1, 2], format_func=lambda x: 'Masculino' if x == 1 else 'Feminino')
educacao = st.selectbox('Educação', options=[1, 2, 3, 4])
estado_civil = st.selectbox('Estado Civil', options=[1, 2, 3])
idade = st.slider('Idade', min_value=18, max_value=100, value=30)

pag_1 = st.selectbox('Pagamento Setembro (PAG_1)', options=range(-2, 9))
pag_2 = st.selectbox('Pagamento Agosto (PAG_2)', options=range(-2, 9))
pag_3 = st.selectbox('Pagamento Julho (PAG_3)', options=range(-2, 9))
pag_4 = st.selectbox('Pagamento Junho (PAG_4)', options=range(-2, 9))
pag_5 = st.selectbox('Pagamento Maio (PAG_5)', options=range(-2, 9))
pag_6 = st.selectbox('Pagamento Abril (PAG_6)', options=range(-2, 9))

fatura_1 = st.number_input('Fatura Setembro', value=0)
fatura_2 = st.number_input('Fatura Agosto', value=0)
fatura_3 = st.number_input('Fatura Julho', value=0)
fatura_4 = st.number_input('Fatura Junho', value=0)
fatura_5 = st.number_input('Fatura Maio', value=0)
fatura_6 = st.number_input('Fatura Abril', value=0)

pagamento_1 = st.number_input('Pagamento Setembro', value=0)
pagamento_2 = st.number_input('Pagamento Agosto', value=0)
pagamento_3 = st.number_input('Pagamento Julho', value=0)
pagamento_4 = st.number_input('Pagamento Junho', value=0)
pagamento_5 = st.number_input('Pagamento Maio', value=0)
pagamento_6 = st.number_input('Pagamento Abril', value=0)

# Botão de previsão
if st.button("Analisar Risco"):
    entrada = pd.DataFrame([[
        limite, sexo, educacao, estado_civil, idade,
        pag_1, pag_2, pag_3, pag_4, pag_5, pag_6,
        fatura_1, fatura_2, fatura_3, fatura_4, fatura_5, fatura_6,
        pagamento_1, pagamento_2, pagamento_3, pagamento_4, pagamento_5, pagamento_6
    ]], columns=colunas)

    predicao = modelo.predict(entrada)[0]
    prob = modelo.predict_proba(entrada)[0][1]

    st.write(f"🧮 Probabilidade de inadimplência: **{prob:.2%}**")
    if predicao == 1:
        st.error("🚨 Cliente com alto risco de inadimplência!")
    else:
        st.success("✅ Cliente com baixo risco de inadimplência.")
