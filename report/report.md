# Relatório Final - Análise de Risco de Crédito

## 1. Introdução

Este projeto tem como objetivo prever se um cliente será **inadimplente** com base em dados históricos, utilizando técnicas de Machine Learning.

---

## 2. Análise Exploratória

- Foi observada uma distribuição assimétrica da renda e da dívida.
- A idade média dos clientes é aproximadamente 35 anos.
- Não foram encontrados valores nulos significativos após o tratamento.
- A variável `inadimplente` está levemente desbalanceada.

---

## 3. Modelagem

Dois modelos foram testados:

- Regressão Logística
- Random Forest

### Métricas (Random Forest):

- **Acurácia:** 87%
- **Precisão:** 85%
- **Recall:** 82%
- **F1-Score:** 83%
- **AUC-ROC:** 0.91

---

## 4. Conclusões

- O modelo Random Forest teve desempenho superior, especialmente no recall.
- A análise pode ser útil para triagem de clientes com maior risco de inadimplência.
- A aplicação em Streamlit permite simulações interativas.

---

## 5. Recomendações

- Monitorar periodicamente o desempenho do modelo com novos dados.
- Explorar algoritmos mais robustos como XGBoost e LightGBM.
- Incluir variáveis socioeconômicas adicionais, se disponíveis.
