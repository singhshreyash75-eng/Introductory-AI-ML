from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(movies, desc):
    descriptions = [m["desc"] for m in movies]

    cv = CountVectorizer(stop_words="english")
    matrix = cv.fit_transform(descriptions)

    similarity = cosine_similarity(matrix)

    idx = descriptions.index(desc)
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:11]

    return [movies[i[0]] for i in scores]