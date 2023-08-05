import streamlit as st
import requests
import pandas as pd
import pickle

def fetch_rating(id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key=a9eebb7876a51cfa80470db01e7a8907')
    data=response.json()
    return data['vote_average']
def fetch_overview(id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key=a9eebb7876a51cfa80470db01e7a8907')
    data=response.json()
    return data['overview']
def fetch_poster(id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key=a9eebb7876a51cfa80470db01e7a8907')
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), key=lambda x: x[1], reverse=True)[1:7]

    recommended_movies=[]
    recommended_movies_posters=[]
    recommended_movies_rating=[]
    recommended_movies_overview = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies['title'][i[0]])
        try:
            recommended_movies_posters.append(fetch_poster(movie_id))
        except:
            recommended_movies_posters.append("https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg")

        recommended_movies_rating.append(str(fetch_rating(movie_id)))
        recommended_movies_overview.append(fetch_overview(movie_id))
    return recommended_movies,recommended_movies_posters,recommended_movies_rating,recommended_movies_overview





movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')
selected_movie = st.selectbox(
    '**Which type of movie you would love to watch** ',
    movies.title.values)



if st.button('Recommend'):
    names,poster ,rating,overview= recommend(selected_movie)

    col1 , col2 = st.columns(2)
    with col1:
        st.subheader(names[0])
        st.image(poster[0])
        st.markdown('**Rating**  : ' + rating[0])
        st.markdown('**Overview** : ' + overview[0])
        st.divider()
    with col2:
        st.subheader(names[1])
        st.image(poster[1])
        st.markdown('**Rating** : ' + rating[1])
        st.markdown('**Overview** : ' + overview[1])
        st.divider()
    with col1:
        st.subheader(names[2])
        st.image(poster[2])
        st.markdown('**Rating** : ' + rating[2])
        st.markdown('**Overview** : ' + overview[2])
        st.divider()
    with col2:
        st.subheader(names[3])
        st.image(poster[3])
        st.markdown('**Rating** : ' + rating[3])
        st.markdown('**Overview** : ' + overview[3])
        st.divider()
    with col1:
        st.subheader(names[4])
        st.image(poster[4])
        st.markdown('**Rating** : ' + rating[4])
        st.markdown('**Overview** : ' + overview[4])
        st.divider()
    with col2:
        st.subheader(names[5])
        st.image(poster[5])
        st.markdown('**Rating** : ' + rating[5])
        st.markdown('**Overview** : ' + overview[5])
        st.divider()





