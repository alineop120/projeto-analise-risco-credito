import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def tratar_valores_nulos(dados):
    """Substitui ou remove valores nulos conforme a estratégia desejada."""
    return dados.dropna()  # ou aplicar imputação

def codificar_variaveis(dados):
    """Codifica variáveis categóricas usando LabelEncoder."""
    codificador = LabelEncoder()
    if 'genero' in dados.columns:
        dados['genero'] = codificador.fit_transform(dados['genero'])
    return dados

def escalar_variaveis(dados, colunas):
    """Aplica StandardScaler nas colunas numéricas."""
    scaler = StandardScaler()
    dados[colunas] = scaler.fit_transform(dados[colunas])
    return dados