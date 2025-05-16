import pandas as pd
from sklearn.preprocessing import StandardScaler

def carregar_dados(caminho):
    """Carrega os dados a partir de um arquivo CSV"""
    return pd.read_csv(caminho)

def limpar_dados(df):
    """Limpa os dados (valores nulos, outliers, etc.)"""
    df = df.fillna(df.mean())
    return df

def codificar_variaveis(df):
    """Codifica variáveis categóricas usando pd.get_dummies"""
    df = pd.get_dummies(df, drop_first=True)
    return df

def escalonar_dados(df):
    """Escalona os dados utilizando StandardScaler"""
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    return df_scaled