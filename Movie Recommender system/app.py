from flask import Flask, render_template, jsonify, request
import json
from model import recommend_movies

app = Flask(__name__)

with open("data/movies.json", encoding="utf-8") as f:
    movies = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/homepage")
def homepage():
    trending = sorted(movies, key=lambda x: x["id"], reverse=True)[:15]
    top = sorted(movies, key=lambda x: x["rating"], reverse=True)[:15]
    return jsonify({"trending": trending, "top": top})

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("movie", "").lower()
    results = [m for m in movies if query in m["title"].lower()]
    return jsonify(results[:20])

@app.route("/movie/<int:id>")
def movie(id):
    m = next((x for x in movies if x["id"] == id), None)
    return jsonify(m if m else {})

@app.route("/recommend/<int:id>")
def recommend(id):
    selected = next((m for m in movies if m["id"] == id), None)
    if not selected:
        return jsonify([])
    return jsonify(recommend_movies(movies, selected["desc"]))

if __name__ == "__main__":
    app.run(debug=True)