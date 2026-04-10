"""Pour la vectorisation du texte et déterminer les mots les plus importants dans les descriptions de poste et les CVs."""

from sklearn.feature_extraction.text import TfidfVectorizer

def get_vectorizer():
    return TfidfVectorizer(max_features=5000)