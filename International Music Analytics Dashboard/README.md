# 🎧 Spotify Top 50 Analytics Dashboard

A sleek and interactive Flask-powered web dashboard that visualizes Spotify’s Top 50 streaming data across multiple countries.  
This project transforms raw CSV datasets into meaningful insights using clean APIs and dynamic visualizations.

---

## 🚀 Overview

This application provides a region-based music analytics system where users can explore:

- 📈 Popularity trends of top songs  
- 🎤 Top artists dominating charts  
- 💿 Album type distribution  
- 🔞 Explicit vs non-explicit content ratio  
- 📊 Tabular breakdown of top tracks  

All data is served through a REST API and can be integrated into any frontend.

---

## 🧠 How It Works

- Flask backend handles requests  
- Pandas processes CSV data  
- Data is cleaned and analyzed dynamically  
- API returns structured JSON  


---

## 🌍 Supported Regions

- World  
- USA  
- UK  
- Spain  
- Korea  
- Mexico  
- Japan  
- France  
- Argentina  
- Italy  

---

## 📊 API Response Example

```json
{
  "region": "USA",
  "popularity_trend": [95, 93, 92],
  "labels": ["Song A", "Song B"],
  "artists": {"Artist A": 3, "Artist B": 2},
  "albums": {"album": 30, "single": 20},
  "explicit": [15, 35],
  "table": [
    {"song": "Song A", "artist": "Artist A", "popularity": 95}
  ]
}

Tech Stack
Python
Flask
Pandas
HTML/CSS
Chart Libraries


project/
│── app.py
│── spotify-streaming-top-50-*.csv
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    └── js/

🛠️ Setup Instructions
Clone the repo
git clone https://github.com/your-username/spotify-analytics-dashboard.git
cd spotify-analytics-dashboard


Install dependencies
pip install flask pandas
Add CSV files in root directory
Run the app
python app.py
Open in browser
http://127.0.0.1:8080

✨ Features
Real-time data processing
Multi-region analytics
Clean API responses
Lightweight backend
Ready for frontend dashboards
⚠️ Error Handling
Missing dataset → 404
Server error → 500
Invalid region → handled safely
💡 Future Improvements
Advanced visualizations
Search & filters
Cloud deployment
ML-based recommendations
Better UI/UX
📌 Highlights
Clean API design
Scalable architecture
Real-world dataset usage
Easy integration
👨‍💻 Author

Built for learning and showcasing data analytics with Flask.

Author - Shreyash Singh
