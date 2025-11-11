import requests
import streamlit as st
import pickle
import pandas as pd

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bcdd39c8aef54f72a6ec979f2ed5ce14&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    # recommended_movies_posters = []
    for i in movies_list:
        movie_id = i[0]
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        # recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommadation System')

Selected_Movie_Name = st.selectbox(
    'Select Movie Name ' ,
    movies['title'].values
)

if st.button('Recommend'):
    recommadation  = recommend(Selected_Movie_Name)
    for i in recommadation:
        st.write(i)




