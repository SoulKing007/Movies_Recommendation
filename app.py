import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a84267440e03d225596aeac62478f84c&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted ( list ( enumerate ( distances ) ), reverse=True, key=lambda x: x[1] )[1:6]

    movies_recommended=[]
    movies_recommended_poster=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        movies_recommended.append(movies.iloc[i[0]].title)
        #fetch poster from api
        movies_recommended_poster.append(fetch_poster(movie_id))

    return movies_recommended,movies_recommended_poster



movie_list = pickle.load(open("C:\\Users\\DELL\\Desktop\\Conda\\Movies_Recommend\\movie-recommender\\.venv\\movie.pkl",'rb'))
movies = pd.DataFrame(movie_list)

similarity = pickle.load(open('C:\\Users\\DELL\\Desktop\\Conda\\Movies_Recommend\\movie-recommender\\.venv\\similarity.pkl','rb'))

original_title = '<p style="font-family:Courier; color:White; font-size: 10px;">Made By Nirav</p>'
st.markdown(original_title,unsafe_allow_html=True)
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Whcih type of movie you want to see?',
movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image ( posters[1] )
    with col3:
        st.text(names[2])
        st.image ( posters[2] )
    with col4:
        st.text(names[3])
        st.image ( posters[3] )
    with col5:
        st.text ( names[4] )
        st.image ( posters[4] )

