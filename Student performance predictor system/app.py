from flask import Flask, render_template, request, jsonify
from model import predict

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def pred():
    data = request.json

    score = predict([
        float(data["hours"]),
        float(data["attendance"]),
        float(data["sleep"])
    ])

    return jsonify({"score": round(score,2)})

if __name__ == "__main__":
    app.run(debug=True) 