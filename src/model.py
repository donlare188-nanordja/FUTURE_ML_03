"""Apres tester différentes approches de model, j'ai opté pour  Linear Regression qui a donné de meilleurs résultats que les autres modèles. Le code ci-dessous montre comment j'ai entraîné le modèle et évalué ses performances. donné le meilleur résultat que les autres modèles. """

from sklearn.linear_model import LogisticRegression

def get_model():
    return LogisticRegression(C=10, solver='liblinear', max_iter=1000)