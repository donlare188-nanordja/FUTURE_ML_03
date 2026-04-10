"""Ce script est utilisé pour faire des prédictions sur de nouveaux CVs en utilisant le modèle entraîné. Il charge le modèle et le vectoriseur, nettoie le texte du CV, le vectorise et fait une prédiction sur la catégorie du CV. Vous pouvez tester la fonction avec un exemple de CV pour voir comment elle fonctionne. """

from utils import load_model
from preprocessing import clean_text

model = load_model("models/model.pkl")
vectorizer = load_model("models/vectorizer.pkl")

def predict_cv(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]

# Test
if __name__ == "__main__":
    sample = "Experienced in Python, Machine Learning, SQL"
    print("Prediction:", predict_cv(sample))