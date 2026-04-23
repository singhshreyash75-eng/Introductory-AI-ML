import json
import random
import os

os.makedirs("data", exist_ok=True)

# 🎬 REAL MOVIES WITH REAL POSTERS (TMDb CDN)
real_movies = [
("Inception","qmDpIHrmpJINaRKAfWQfftjCdyi.jpg"),
("The Dark Knight","qJ2tW6WMUDux911r6m7haRef0WH.jpg"),
("Interstellar","rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg"),
("Parasite","7IiTTgloJzvGI1TAYymCfbfl3vT.jpg"),
("3 Idiots","66A9MqXOyVFCssoloscw79z8Tew.jpg"),
("Avengers Endgame","or06FN3Dka5tukK1e9sl16pB3iy.jpg"),
("Joker","udDclJoHjfjb8Ekgsd4FDteOkCU.jpg"),
("The Shawshank Redemption","q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg"),
("The Godfather","3bhkrj58Vtu7enYsRolD1fZdja1.jpg"),
("Fight Club","bptfVGEQuv6vDTIMVCHjJ9Dz8PX.jpg"),
("La La Land","uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg"),
("Dangal","p2lVAcPuRPSO8Al6hDDGw0OgMiQ.jpg"),
("Spirited Away","39wmItIWsg5sZMyRUHLkWBcuVCM.jpg"),
("The Matrix","f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"),
("Gladiator","ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg"),
("Titanic","9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg"),
("Avatar","kyeqWdyUXW608qlYkRqosgbbJyK.jpg"),
("Whiplash","6uSPcdGNA2A6vJmCagXkvnutegs.jpg"),
("Dune","d5NXSklXo0qyIYkgV94XAgMIckC.jpg"),
("Oppenheimer","8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg"),
]

genres = ["Action","Drama","Comedy","Thriller","Sci-Fi","Romance","Horror","Adventure","Animation"]
languages = ["English","Hindi","Korean","Japanese","Spanish","French"]

movies = []

# ✅ ADD REAL MOVIES FIRST
for i, (title, poster_path) in enumerate(real_movies, start=1):
    movies.append({
        "id": i,
        "title": title,
        "genre": ", ".join(random.sample(genres, 2)),
        "language": random.choice(languages),
        "rating": round(random.uniform(7.5, 9.3), 1),
        "desc": f"{title} is a critically acclaimed film known for its powerful storytelling and strong performances.",
        "poster": f"https://image.tmdb.org/t/p/w500/{poster_path}"
    })

# 🎬 ADD MORE REAL TITLES (WITHOUT POSTERS)
more_titles = [
"Arrival","Blade Runner 2049","Mad Max Fury Road","Tenet","The Martian",
"Gravity","The Revenant","Django Unchained","Inglourious Basterds",
"Once Upon a Time in Hollywood","The Wolf of Wall Street",
"The Social Network","Catch Me If You Can","The Truman Show",
"Shutter Island","Get Out","A Quiet Place","The Conjuring",
"Insidious","Annabelle","It","Hereditary",
"Toy Story","Finding Nemo","Coco","Up","Frozen",
"Moana","Encanto","Zootopia","Ratatouille","WALL-E"
]

start_id = len(movies) + 1

for i, title in enumerate(more_titles, start=start_id):
    movies.append({
        "id": i,
        "title": title,
        "genre": ", ".join(random.sample(genres, 2)),
        "language": random.choice(languages),
        "rating": round(random.uniform(6.5, 8.8), 1),
        "desc": f"{title} tells a compelling story filled with emotion, conflict, and memorable moments.",
        "poster": f"https://dummyimage.com/300x450/222/fff&text={title.replace(' ','+')}"
    })

# 💾 SAVE
with open("data/movies.json", "w") as f:
    json.dump(movies, f, indent=4)

print(f"✅ Dataset ready with {len(movies)} real movies!")