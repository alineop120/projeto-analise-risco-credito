<h1 align="center">📈 Relatório Técnico dos Modelos</h1>
<p align="center">Avaliação comparativa dos algoritmos treinados para previsão de inadimplência</p>
<hr/>

<h2>🧪 Dados Utilizados</h2>
<ul>
  <li><strong>Fonte:</strong> UCI German Credit Dataset</li>
  <li><strong>Tipo:</strong> Classificação binária (0 = adimplente, 1 = inadimplente)</li>
  <li><strong>Quantidade:</strong> 1000 amostras, 20 variáveis preditoras + 1 alvo</li>
  <li><strong>Pré-processamento:</strong> ColumnTransformer, escalonamento, OneHotEncoder, SMOTENC para balanceamento</li>
</ul>

<h2>🧠 Modelos Treinados</h2>
<p>Todos os modelos foram otimizados usando <code>RandomizedSearchCV</code> com <code>StratifiedKFold (n=10)</code> e validação baseada em diferentes métricas de avaliação.</p>

<h3>📌 Métricas Utilizadas</h3>
<ul>
  <li><strong>Accuracy:</strong> porcentagem de acertos</li>
  <li><strong>Precision:</strong> % de previsões positivas que estavam corretas</li>
  <li><strong>Recall:</strong> % de inadimplentes que foram corretamente detectados</li>
  <li><strong>F1-score:</strong> equilíbrio entre precisão e recall</li>
  <li><strong>ROC AUC:</strong> capacidade de separação do modelo</li>
  <li><strong>Average Precision:</strong> área sob a curva precision-recall</li>
</ul>

<h2>📊 Comparativo de Modelos</h2>
<table>
  <thead>
    <tr>
      <th>Modelo</th>
      <th>Accuracy</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1</th>
      <th>ROC AUC</th>
      <th>Avg Precision</th>
      <th>Tempo Treino (s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Regressão Logística</strong></td>
      <td>70.0%</td>
      <td>81.25%</td>
      <td>74.29%</td>
      <td>0.776</td>
      <td>0.753</td>
      <td>0.870</td>
      <td>1064.7</td>
    </tr>
    <tr>
      <td><strong>Random Forest</strong></td>
      <td>71.5%</td>
      <td>79.02%</td>
      <td>80.71%</td>
      <td>0.799</td>
      <td>0.784</td>
      <td>0.900</td>
      <td>1086.0</td>
    </tr>
    <tr>
      <td><strong>XGBoost</strong></td>
      <td>70.0%</td>
      <td>77.78%</td>
      <td>80.00%</td>
      <td>0.789</td>
      <td>0.726</td>
      <td>0.846</td>
      <td>1088.1</td>
    </tr>
    <tr>
      <td><strong>LightGBM</strong></td>
      <td>72.5%</td>
      <td>80.58%</td>
      <td>80.00%</td>
      <td>0.803</td>
      <td>0.745</td>
      <td>0.864</td>
      <td>1130.2</td>
    </tr>
  </tbody>
</table>

<h2>🏆 Conclusão</h2>
<ul>
  <li><strong>Melhor F1-Score:</strong> LightGBM (0.803)</li>
  <li><strong>Melhor ROC AUC:</strong> Random Forest (0.784)</li>
  <li><strong>Melhor Precision:</strong> Regressão Logística (81.25%)</li>
  <li><strong>Melhor Average Precision:</strong> Random Forest (0.900)</li>
</ul>

<h3>✅ Modelo Recomendado</h3>
<p><strong>Random Forest</strong> demonstrou o melhor equilíbrio entre desempenho e robustez, especialmente em curvas ROC e precision-recall.</p>

<h2>📁 Parâmetros Otimizados</h2>
<h4>🔹 Random Forest</h4>
<ul>
  <li>n_estimators = 430</li>
  <li>max_depth = 44</li>
  <li>min_samples_split = 6</li>
  <li>min_samples_leaf = 1</li>
</ul>

<h4>🔹 XGBoost</h4>
<ul>
  <li>n_estimators = 221</li>
  <li>learning_rate = 0.173</li>
  <li>max_depth = 5</li>
  <li>subsample = 0.757</li>
  <li>colsample_bytree = 0.648</li>
</ul>

<h4>🔹 LightGBM</h4>
<ul>
  <li>n_estimators = 164</li>
  <li>learning_rate = 0.031</li>
  <li>max_depth = 7</li>
  <li>num_leaves = 86</li>
</ul>

<h4>🔹 Regressão Logística</h4>
<ul>
  <li>C = 56.7</li>
</ul>

<h2>📂 Origem das Métricas</h2>
<ul>
  <li>Arquivo: <code>all_models.ipynb</code></li>
  <li>Validação cruzada estratificada (10 folds)</li>
  <li>Resultados salvos em: <code>models/*.json</code></li>
</ul>

<h2>📌 Observações Técnicas</h2>
<ul>
  <li>Aplicação final consome os modelos via Streamlit (<code>app.py</code>)</li>
  <li>Todos os modelos utilizam <code>SMOTENC</code> para tratamento de desbalanceamento</li>
  <li>Pipeline modular com <code>Pipeline</code> + <code>ColumnTransformer</code></li>
</ul>