from flask import Flask, render_template, request
import pickle
import pandas as pd
import requests
import time

app = Flask(__name__)

API_KEY = "30c5be2de005151651073ac99a697153"

# ---------------- FETCH POSTER ---------------- #
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=No+Image"

        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    except:
        return "https://via.placeholder.com/500x750?text=Error"


# ---------------- LOAD DATA ---------------- #
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# ---------------- RECOMMEND FUNCTION ---------------- #
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

        poster = fetch_poster(movie_id)
        recommended_movies_posters.append(poster)

        time.sleep(0.2)

    return recommended_movies, recommended_movies_posters


# ---------------- ROUTES ---------------- #
@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_movies = []
    recommended_posters = []

    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        recommended_movies, recommended_posters = recommend(selected_movie)

    return render_template(
        'index.html',
        movies=movies['title'].values,
        names=recommended_movies,
        posters=recommended_posters
    )


# ---------------- RUN ---------------- #
if __name__ == '__main__':
    app.run(debug=True)