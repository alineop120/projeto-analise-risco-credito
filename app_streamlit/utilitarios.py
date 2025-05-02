import pandas as pd
import joblib

def carregar_modelo(caminho_modelo):
    """Carrega modelo treinado em formato .pkl"""
    return joblib.load(caminho_modelo)

def preparar_entrada(idade, renda, divida, genero):
    """Prepara o DataFrame de entrada para a previsão"""
    genero_codificado = 1 if genero == 'Masculino' else 0
    dados = pd.DataFrame([[idade, renda, divida, genero_codificado]],
                         columns=['idade', 'renda', 'divida', 'genero'])
    return dados