# 🎓 Student Performance Detector

A lightweight **Machine Learning web application** that predicts a student’s exam performance using study habits and lifestyle inputs. Built with **Flask + Scikit-learn**, this project demonstrates an end-to-end ML workflow with a clean, responsive UI.

---

## ✨ Highlights

* ⚡ **Instant predictions** from user inputs
* 🧠 **Regression-based ML model** for score estimation
* 🌐 **Flask backend** with real-time API endpoint
* 🎨 Minimal, responsive **UI**
* 🏆 **Automatic grading** (A / B / C)
* 🧩 Fully **offline** (no external APIs)

---

## 🧠 How It Works

1. User enters:

   * Study Hours
   * Attendance (%)
   * Sleep Hours

2. Frontend sends data to the backend (`/predict` endpoint)

3. A trained **Linear Regression** model processes the inputs

4. The system returns:

   * **Predicted Score**
   * **Grade Classification**

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **ML:** Scikit-learn
* **Model:** Linear Regression

---

## 📁 Project Structure

```text id="mjfyib"
student-performance-detector/
│── app.py
│── model.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ Setup & Run

1. **Clone the repo**

```bash id="1l3hij"
git clone https://github.com/your-username/student-performance-detector.git
cd student-performance-detector
```

2. **Install dependencies**

```bash id="v4r0c0"
pip install flask scikit-learn
```

3. **Run the app**

```bash id="5npl0d"
python app.py
```

4. **Open in browser**

```text id="r3w1xw"
http://localhost:5000
```

---

## 📊 Example

**Input:**

* Study Hours: 8
* Attendance: 75%
* Sleep: 6 hrs

**Output:**

* Predicted Score: **~65**
* Grade: **B**

---

## 🎯 Use Cases

* Academic performance estimation
* Basic analytics for study habits
* Demonstration of ML deployment in web apps

---

## 🚧 Limitations

* Uses a small/sample dataset
* Linear model → limited complexity
* Predictions are indicative, not definitive

---

## 🔮 Future Scope

* Add multiple models (Random Forest, Decision Tree)
* Show evaluation metrics (R², MAE)
* Visualize trends with charts
* Allow CSV dataset upload & retraining

---

## 👨‍💻 Author

**Shreyash Singh**

---

## ⭐ Support

If you found this useful, consider giving it a **star ⭐** and sharing feedback!
