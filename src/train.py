"""Ce script est le cœur de notre projet de screening de CV. Il intègre toutes les étapes clés du pipeline, depuis le chargement des données jusqu'à l'entraînement du modèle, l'évaluation et le classement des candidats. Voici un aperçu détaillé de chaque étape :"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics.pairwise import cosine_similarity

from preprocessing import clean_text
from feature_engineering import get_vectorizer
from model import get_model
from ranking import compute_final_score
from utils import save_model

# =========================
# 1. Load data
# =========================
df = pd.read_csv("data/raw/UpdatedResumeDataSet.csv")

# =========================
# 2. Preprocessing
# =========================
df['clean_resume'] = df['Resume'].apply(clean_text)

# =========================
# 3. Feature Engineering
# =========================
vectorizer = get_vectorizer()
X = vectorizer.fit_transform(df['clean_resume'])
y = df['Category']

# =========================
# 4. Train / Test Split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 5. Train Model
# =========================
model = get_model()
model.fit(X_train, y_train)

# =========================
# 6. Evaluation
# =========================
y_pred = model.predict(X_test)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# =========================
# 7. Matching 
# =========================
job_description = """
Looking for a Data Scientist with Python, Machine Learning,
SQL, Data Analysis and Deep Learning experience.
"""

job_vec = vectorizer.transform([job_description])
cv_vecs = vectorizer.transform(df['clean_resume'])

df['match_score'] = cosine_similarity(job_vec, cv_vecs).flatten()

# =========================
# 8. Smart Ranking
# =========================
skills = ["python", "machine learning", "sql", "data analysis"]

df = compute_final_score(df, "Data Science", skills)

df = df.sort_values(by="final_score", ascending=False)

# =========================
# 9. Save Outputs
# =========================
df[['Category', 'final_score']].to_csv("outputs/ranking.csv", index=False)

# =========================
# 10. Save Models
# =========================
save_model(model, "models/model.pkl")
save_model(vectorizer, "models/vectorizer.pkl")

print("\n Training + Ranking terminé avec succès !")