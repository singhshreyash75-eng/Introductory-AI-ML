# 🎬 Movie Recommendation System

A sleek, Netflix-inspired movie recommendation web app built using **Flask + Machine Learning**.
This project provides personalized movie suggestions based on content similarity, with a clean and interactive UI.

---

## 🚀 Features

* 🔍 Search movies instantly
* 🎯 Content-based recommendation system
* 🔥 Trending & ⭐ Top Rated sections
* 🎨 Netflix-style UI with banner display
* 🖼️ Poster support with fallback handling
* ⚡ Fast and fully offline (no API dependency)

---

## 🧠 How It Works

This project uses a **Content-Based Filtering** approach:

* Movie descriptions are vectorized using `CountVectorizer`
* Cosine similarity is calculated between movies
* Based on selected movie → similar movies are recommended

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask (Python)
* **ML Logic:** Scikit-learn (Cosine Similarity)
* **Dataset:** Custom curated movie dataset

---

## 📁 Project Structure

```
movie_app/
│── app.py
│── model.py
│
├── data/
│   └── movies.json
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

2. Install dependencies

```bash
pip install flask scikit-learn
```

3. Run the app

```bash
python app.py
```

4. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📸 Preview

* Homepage with trending & top-rated movies
* Dynamic banner with movie details
* Recommendation system in action

---

## 🎯 Future Improvements

* User login & watchlist
* Genre-based filtering
* Real-time API integration (optional)
* Trailer integration

---

## 💡 Author

**Shrey Boss**

---

## ⭐ If you like this project

Give it a star ⭐ and share feedback!
