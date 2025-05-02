<div align="center">
  <h1>🔍 Análise de Risco de Crédito - Previsão de Inadimplência</h1>
  <p>Projeto de machine learning para previsão de inadimplência em operações de crédito</p>
</div>

<h2>📋 Objetivos</h2>
<ul>
  <li>Exercitar técnicas de limpeza e análise de dados com Pandas</li>
  <li>Desenvolver análise exploratória (EDA) com visualizações</li>
  <li>Implementar modelos de classificação (Regressão Logística, Random Forest)</li>
  <li>Avaliar métricas de performance (AUC-ROC, precisão, recall)</li>
  <li>Criar interface interativa com Streamlit</li>
</ul>

<h2>🛠️ Tecnologias Utilizadas</h2>
<div class="tech-stack">
  <div class="tech-category">
    <div class="tech-icon">
      <h3>Análise de Dados</h3>
    </div>
    <ul>
      <li title="Pandas">
        <span>Pandas</span>
      </li>
      <li title="NumPy">
        <span>NumPy</span>
      </li>
      <li title="Visualização">
        <span>Matplotlib/Seaborn</span>
      </li>
    </ul>
  </div>
  
  <div class="tech-category">
    <div class="tech-icon">
      <h3>Machine Learning</h3>
    </div>
    <ul>
      <li title="Scikit-learn">
        <span>Scikit-learn</span>
      </li>
      <li title="XGBoost">
        <span>XGBoost</span>
      </li>
    </ul>
  </div>
  
  <div class="tech-category">
    <div class="tech-icon">
      <h3>Desenvolvimento</h3>
    </div>
    <ul>
      <li title="Python">
        <span>Python</span>
      </li>
      <li title="Jupyter">
        <span>Jupyter</span>
      </li>
      <li title="Streamlit">
        <span>Streamlit</span>
      </li>
    </ul>
  </div>
</div>


<h2>📁 Estrutura do Projeto</h2>
<pre>
analise-risco-credito/
├── dados/               # Dados brutos e processados
├── notebooks/           # Jupyter Notebooks (EDA e modelagem)
│   ├── analise_exploratoria.ipynb
│   └── treinamento_modelos.ipynb
├── scripts/            # Funções utilitárias
├── app/                # Aplicativo Streamlit
│   └── app.py
├── resultados/         # Modelos e figuras
│   ├── modelos/
│   └── visualizacoes/
├── relatorio/          # Documentação final
└── requirements.txt    # Dependências
</pre>

<h2>⚙️ Configuração do Ambiente</h2>
<ol>
  <li>Clone o repositório:
    <pre><code>git clone https://github.com/alineop120/projeto-analise-risco-credito.git
cd projeto-analise-risco-credito</code></pre>
  </li>
  <li>Crie e ative o ambiente virtual:
    <pre><code>1. python -m venv .venv<br>
2.  source .venv/bin/activate  # Linux/Mac
    .venv\Scripts\activate     # Windows</code></pre>
  </li>
  <li>Instale as dependências:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ol>

<h2>🚀 Execução</h2>
<h3>Análise Exploratória</h3>
<pre><code>jupyter notebook notebooks/analise_exploratoria.ipynb</code></pre>

<h3>Treinamento dos Modelos</h3>
<pre><code>jupyter notebook notebooks/treinamento_modelos.ipynb</code></pre>

<h3>Aplicativo Streamlit</h3>
<pre><code>streamlit run app/app.py</code></pre>

<h2>📊 Modelos Implementados</h2>
<div class="model-grid">
  <div>
    <h3>Regressão Logística</h3>
    <ul>
      <li>Acurácia: 0.78</li>
      <li>Precisão: 0.82</li>
      <li>Recall: 0.71</li>
      <li>AUC-ROC: 0.85</li>
    </ul>
  </div>
  <div>
    <h3>Random Forest</h3>
    <ul>
      <li>Acurácia: 0.81</li>
      <li>Precisão: 0.84</li>
      <li>Recall: 0.75</li>
      <li>AUC-ROC: 0.88</li>
    </ul>
  </div>
</div>

<h2>📌 Variáveis Utilizadas</h2>
<div align="center">
    <table>
    <tr>
        <th>Categoria</th>
        <th>Variáveis</th>
    </tr>
    <tr>
        <td>Dados Demográficos</td>
        <td>SEXO, EDUCACAO, ESTADO_CIVIL, IDADE</td>
    </tr>
    <tr>
        <td>Histórico de Pagamentos</td>
        <td>PAG_1 a PAG_6, PAGAMENTO_1 a PAGAMENTO_6</td>
    </tr>
    <tr>
        <td>Informações Financeiras</td>
        <td>LIMIT_BAL, FATURA_1 a FATURA_6</td>
    </tr>
    </table>
</div>

<h2>👥 Equipe</h2>
<div align="center">
  <p>Projeto desenvolvido por alunos do curso de Ciência da Computação da Universidade Católica de Brasília (UCB)</p>
<table>
  <tr>
    <th>Nome</th>
    <th>Matrícula</th>
    <th>GitHub</th>
  </tr>
  <tr>
    <td>Aline Oliveira</td>
    <td>UC23101158</td>
    <td><a href="https://github.com/alineop120">@alineop120</a></td>
  </tr>
  <tr>
    <td>João Victor</td>
    <td>UC23103118</td>
    <td><a href="https://github.com/itsryu">@itsryu</a></td>
  </tr>
  <tr>
    <td>Ana Beatriz</td>
    <td>UC23101592</td>
    <td><a href="https://github.com/Anabamorim">@Anabamorim</a></td>
  </tr>
  <tr>
    <td>Cristhiane Tamilly</td>
    <td>UC23200044</td>
    <td><a href="https://github.com/ctamilly">@ctamilly</a></td>
  </tr>
</table>
</div>

<h2>📚 Fontes de Dados</h2>
<ul>
  <li><a href="https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset">Kaggle - Default of Credit Card Clients</a></li>
  <li><a href="https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients">UCI - Default of Credit Card Clients</a></li>
  <li><a href="https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)">UCI - German Credit Data</a></li>
</ul>

<h2>📄 Referências</h2>
<ul>
  <li>Geron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow. O'Reilly Media.</li>
  <li>Raschka, S., & Mirjalili, V. (2019). Python Machine Learning. Packt Publishing.</li>
  <li>Brownlee, J. (2018). Machine Learning Mastery with Python. Machine Learning Mastery.</li>
  <li>Scikit-learn Documentation. (2023). Retrieved from <a href="https://scikit-learn.org/stable/">scikit-learn.org</a></li>
    <li>Streamlit Documentation. (2023). Retrieved from <a href="https://docs.streamlit.io/">streamlit.io</a></li>
</ul>