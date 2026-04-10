"""Ce module contient les fonctions pour calculer le score final de chaque candidat en combinant la similarité de texte, la correspondance des compétences et la catégorie prédite. Le score final est utilisé pour classer les candidats et identifier les meilleurs profils pour le poste. """

def skill_score(text, skills):
    text = text.lower()
    return sum([1 for s in skills if s in text]) / len(skills)

def category_bonus(predicted, target):
    return 1 if predicted == target else 0

def compute_final_score(df, target_category, skills):
    
    scores = []
    
    for _, row in df.iterrows():
        sim = row['match_score']
        skill = skill_score(row['Resume'], skills)
        cat = category_bonus(row['Category'], target_category)
        
        final = 0.6 * sim + 0.3 * skill + 0.1 * cat
        scores.append(final)
    
    df['final_score'] = scores
    return df