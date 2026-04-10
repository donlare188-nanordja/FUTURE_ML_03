""""Ce module contient des fonctions utilitaires pour sauvegarder et charger les modèles entraînés, ainsi que pour d'autres tâches de manipulation de données ou de modèles. """

import joblib

def save_model(model, path):
    joblib.dump(model, path)

def load_model(path):
    return joblib.load(path)