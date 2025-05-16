from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

def treinar_random_forest(X_train, y_train):
    """Treina o modelo Random Forest"""
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    return modelo

def treinar_regressao_logistica(X_train, y_train):
    """Treina o modelo de Regressão Logística"""
    modelo = LogisticRegression()
    modelo.fit(X_train, y_train)
    return modelo

def avaliar_modelo(modelo, X_test, y_test):
    """Avalia o modelo com base nas métricas de performance"""
    y_pred = modelo.predict(X_test)
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("Relatório de Classificação:\n", classification_report(y_test, y_pred))