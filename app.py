import streamlit as st
import pickle
import pandas as pd
import requests
import json

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{0}?api_key=d61204e42321cddd34e0f954c0bf649f&language=en-US'.format(movie_id))
    data = response.json()
    return  "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
def recomend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recomendedMovies = []
    recomended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recomendedMovies.append(movies.iloc[i[0]].title)
        recomended_movies_posters.append(fetch_poster(movie_id))
    return  recomendedMovies, recomended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
st.title('Moive Recomender System')
selected_movie = st.selectbox(
    'How you would like to be connected', movies['title'].values)

if st.button('Recomend'):
    recomend_movies, poster = recomend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recomend_movies[0])
        st.image(poster[0])
    with col2:
        st.text(recomend_movies[1])
        st.image(poster[1])
    with col3:
        st.text(recomend_movies[2])
        st.image(poster[2])
    with col4:
        st.text(recomend_movies[3])
        st.image(poster[3])
    with col5:
        st.text(recomend_movies[4])
        st.image(poster[4])


