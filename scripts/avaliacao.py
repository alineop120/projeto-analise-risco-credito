from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score


def avaliar_modelo(modelo, X_teste, y_teste):
    """Exibe as métricas principais de avaliação do modelo."""
    y_pred = modelo.predict(X_teste)
    print("Relatório de Classificação:")
    print(classification_report(y_teste, y_pred))
    print("Matriz de Confusão:")
    print(confusion_matrix(y_teste, y_pred))
    try:
        probas = modelo.predict_proba(X_teste)[:, 1]
        print("AUC-ROC:", roc_auc_score(y_teste, probas))
    except:
        print("Modelo não suporta predict_proba.")
