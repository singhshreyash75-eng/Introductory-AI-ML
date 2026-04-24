import pandas as pd
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Dictionary to map regions to your actual filenames
REGIONS = {
    'world': 'spotify-streaming-top-50-world.csv',
    'usa': 'spotify-streaming-top-50-usa.csv',
    'uk': 'spotify-streaming-top-50-uk.csv',
    'spain': 'spotify-streaming-top-50-spain.csv',
    'korea': 'spotify-streaming-top-50-korea.csv',
    'mexico': 'spotify-streaming-top-50-mexico.csv',
    'japan': 'spotify-streaming-top-50-japan.csv',
    'france': 'spotify-streaming-top-50-france.csv',
    'argentina': 'spotify-streaming-top-50-argentina.csv',
    'italy': 'spotify-streaming-top-50-italy.csv'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats/<region>')
def get_stats(region):
    filename = REGIONS.get(region)
    
    if not filename or not os.path.exists(filename):
        return jsonify({"error": f"File '{filename}' missing"}), 404

    try:
        df = pd.read_csv(filename)
        
        # Data Cleaning: Convert popularity to numeric to avoid flat lines
        df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce').fillna(0)
        
        # Get Top 10 for Trend
        top_10_df = df.head(10)
        pop_trend = top_10_df['popularity'].astype(int).tolist()
        song_labels = top_10_df['song'].tolist()
        
        # Stats for other charts
        top_artists = df['artist'].value_counts().head(5).to_dict()
        album_dist = df['album_type'].value_counts().to_dict()
        ex_counts = df['is_explicit'].value_counts().to_dict()
        
        table_data = top_10_df[['song', 'artist', 'popularity']].to_dict(orient='records')

        return jsonify({
            "region": region.upper(),
            "popularity_trend": pop_trend,
            "labels": song_labels,
            "artists": top_artists,
            "albums": album_dist,
            "explicit": [ex_counts.get(True, 0), ex_counts.get(False, 0)],
            "table": table_data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)