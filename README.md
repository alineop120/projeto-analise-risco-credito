# Análise de Risco de Crédito

Projeto de aprendizado supervisionado para prever inadimplência de clientes com base em dados históricos.

## 📁 Estrutura do Projeto
```
analise-risco-credito/
├── dados/ # Dados brutos e tratados 
├── notebooks/ # Jupyter Notebooks de EDA e modelagem
├── scripts/ # Scripts Python para reuso de funções 
├── app_streamlit/ # Aplicativo interativo com Streamlit 
├── resultados/ # Modelos e figuras geradas 
├── relatorio/ # Relatório final do projeto 
├── requirements.txt # Dependências do projeto 
└── README.md # Este arquivo
```

---

## ⚙️ Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/analise-risco-credito.git
```

2. Instale os requisitos:
pip install -r requirements.txt

3. Execute o notebook de análise e o de modelagem: analise_exploratoria e treinamento_modelos (nessa ordem)

4. Para rodar o app Streamlit:
streamlit run app_streamlit/app.py


---

## 📊 Objetivo

Utilizar modelos de classificação (como Regressão Logística e Random Forest) para prever a variável inadimplente.

🧪 Métricas de Avaliação
* Acurácia
* Precisão
* Recall
* F1-score
* AUC-ROC

---

## 💾 Treinamento e Salvamento de Modelos

No notebook `notebooks/treinamento_modelos.ipynb`, após treinar os modelos, salve os arquivos necessários:

```python
import joblib
import os

os.makedirs('../resultados/modelos', exist_ok=True)
joblib.dump(modelo_rf, '../resultados/modelos/modelo_rf.pkl')
joblib.dump(X.columns, '../resultados/modelos/colunas_treinamento.pkl')
```

Se estiver usando regressão logística com dados escalonados:

```python
joblib.dump(scaler, '../resultados/modelos/escalonador.pkl')
```


## 🖥️ App Streamlit – Entrada de Dados
O app espera 23 variáveis, na mesma ordem usada durante o treinamento. São elas:

* LIMIT_BAL, SEXO, EDUCACAO, ESTADO_CIVIL, IDADE
* PAG_1 até PAG_6
* FATURA_1 até FATURA_6
* PAGAMENTO_1 até PAGAMENTO_6

No app, organize os dados assim:

```python
entrada = pd.DataFrame([[
    limite, sexo, educacao, estado_civil, idade,
    pag_1, pag_2, pag_3, pag_4, pag_5, pag_6,
    fatura_1, fatura_2, fatura_3, fatura_4, fatura_5, fatura_6,
    pagamento_1, pagamento_2, pagamento_3, pagamento_4, pagamento_5, pagamento_6
]], columns=colunas)
```

Essas colunas são carregadas via:

```python
colunas = joblib.load('../resultados/modelos/colunas_treinamento.pkl')
```

## ✅ Resultado Esperado
```
🧮 Probabilidade de inadimplência: 42.7%
🚨 Cliente com alto risco de inadimplência!
```