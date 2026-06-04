# 🚀 AI Tech Stack Recommender

An AI-powered recommendation system that analyzes user skills and interests to suggest the most suitable technology domains and career paths. The project uses **TF-IDF Vectorization** and **Cosine Similarity** to generate intelligent recommendations with match percentages.

## 📌 Features

* 🔍 Skill-based career recommendations
* 🤖 AI-powered similarity matching
* 📊 Match percentage scoring
* 🎨 Modern Glassmorphism UI
* 📱 Fully responsive design
* ⚡ Fast and lightweight Flask application

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

### Data Processing

* Pandas

---

## 📂 Project Structure

```text
AI-Tech-Stack-Recommender/
│
├── app.py
├── requirements.txt
├── skills_dataset.csv
│
├── templates/
│   └── index.html
│
└──  static/
   └── style.css

```

---

## ⚙️ Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User enters skills and interests.
2. Skills are converted into numerical vectors using TF-IDF.
3. Cosine Similarity compares user skills with predefined career profiles.
4. Top matching career paths are displayed with similarity scores.

---

## 📸 Example Input

```text
Python Machine Learning SQL
```

### Example Output

```text
Data Scientist      - 95%
AI Engineer         - 88%
Machine Learning Engineer - 84%
```

---

## 🎯 Learning Outcomes

* Recommendation System Fundamentals
* Natural Language Processing Concepts
* TF-IDF Vectorization
* Cosine Similarity
* Flask Web Development
* User Interface Design

---

## 🌟 Future Enhancements

* User Authentication
* Database Integration
* Skill Auto-Suggestions
* Interactive Charts
* Career Roadmaps
* Resume Skill Analyzer
* AI-Powered Skill Gap Analysis

---

## 👨‍💻 Author

**Dheeraj**

---

## 📜 License

This project is developed for educational and internship purposes under the DecodeLabs Artificial Intelligence Training Program.
