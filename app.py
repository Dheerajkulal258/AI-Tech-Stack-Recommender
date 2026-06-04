from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

df = pd.read_csv("skills_dataset.csv")

vectorizer = TfidfVectorizer()

skill_vectors = vectorizer.fit_transform(df["Skills"])

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    if request.method == "POST":
        user_skills = request.form["skills"]

        user_vector = vectorizer.transform([user_skills])

        similarity_scores = cosine_similarity(
            user_vector,
            skill_vectors
        )

        scores = similarity_scores.flatten()

        top_indices = scores.argsort()[-3:][::-1]

        recommendations = []

        for index in top_indices:
            recommendations.append({
                "role": df.iloc[index]["Role"],
                "score": round(scores[index] * 100, 1)
            })

    return render_template(
        "index.html",
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)