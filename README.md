# 🧠 Resume Screening & Ranking System (AI-Powered)

## 🚀 Project Overview

This project is an **end-to-end Machine Learning system** designed to automate the recruitment process by:

* 📄 Classifying resumes into job categories
* 🎯 Matching resumes with job descriptions
* 🏆 Ranking candidates based on relevance

👉 The goal is to **help recruiters save time, reduce costs, and make smarter hiring decisions**.

## 🧩 Key Features

✔ Resume classification using Machine Learning
✔ TF-IDF based text vectorization
✔ Job description matching (cosine similarity)
✔ Smart ranking system combining:

* Semantic similarity
* Skill matching
* Category alignment

✔ Exploratory Data Analysis (EDA) with visual insights
✔ NLP analysis (WordCloud, top keywords per category)

## 🧠 Tech Stack

* Python 🐍
* Scikit-learn
* Pandas / NumPy
* Matplotlib / Seaborn
* NLP (TF-IDF)
* Power BI (for visualization)

## 📊 Project Workflow

1. Data loading & preprocessing
2. Text cleaning & normalization
3. Feature extraction (TF-IDF)
4. Model training (Logistic Regression + others)
5. Model evaluation & optimization (GridSearchCV)
6. Resume classification
7. Job matching (cosine similarity)
8. Smart ranking system

## 🏆 Smart Ranking Formula

The final candidate score is computed as:

Score =
0.6 × Similarity Score

* 0.3 × Skill Matching Score
* 0.1 × Category Match Bonus

👉 This makes the system more **intelligent and business-oriented**.

## 📂 Project Structure

```
resume-screening/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
├── notebooks/
│   └── exploration.ipynb
│
├── outputs/
│   ├── visualizations
│   └── ranking.csv
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── ranking.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── environment.yml
└── README.md
```

---

## 📈 Sample Outputs

* 📊 Category distribution
* 📉 Resume length analysis
* ☁️ WordCloud per job category
* 🏆 Candidate ranking (Top matches)

## ⚙️ How to Run

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/resume-screening.git
cd resume-screening
```

### 2. Create environment

```
conda env create -f environment.yml
conda activate cv_matching
```

### 3. Train the model

```
cd src
python src/train.py
```

### 4. Predict

python src/predict.py

## 📌 Important Note

⚠️ This repository contains a **simplified version** of the system.

* Dataset is not included
* Trained models are not included

👉 The **full production version (with advanced models and extended dataset)** is private.

## 🚀 Future Improvements

* 🔥 Deep Learning models (BERT, Transformers)
* 🌐 Web application (Streamlit / FastAPI)
* 📊 Advanced dashboards (Power BI)
* 🤖 Automated candidate recommendation system

## 💼 Business Value

This system can:

* ⏱ Reduce recruitment time
* 💰 Lower hiring costs
* 🎯 Improve candidate-job matching
* 📊 Assist HR decision-making

## 🤝 Let's Connect

If you're interested in this project or collaboration:

* 💼 LinkedIn: linkedin.com/in/donné-lare-4491693b1
* 📧 Email: don188@gmail.com

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
