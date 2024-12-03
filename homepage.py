from logging import exception
import spotipy
from PIL import Image
from io import BytesIO
import requests
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
from my_secrets import SPOTIFY_CLIENT_ID,SPOTIFY_CLIENT_SECRET,SCOPE
from emotion_detector import processing,feedback_form
from song_player import query
import webbrowser
memory=st.session_state
st.set_page_config(layout="wide",page_title="MoodMelody",page_icon=":musical_note:",initial_sidebar_state="expanded")
redirect_url = "http://localhost:8501/"
sp_oauth = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,client_secret=SPOTIFY_CLIENT_SECRET,redirect_uri=redirect_url, scope=SCOPE,cache_path=".cache")
if "code" not in st.query_params:

    auth_url = sp_oauth.get_authorize_url()
    webbrowser.open(auth_url,new=0,autoraise=False)

else:
    token_info = sp_oauth.get_access_token( st.query_params["code"], as_dict=False)
    sp = spotipy.Spotify(auth=token_info)
    def emotion_detector():
        memory.page="emotion_detection"

    try :
        if memory.page=="":
            pass
    except BaseException or exception as e:
        memory.page='home'
    if memory.page=='song':

        feedback_form()
        query(sp,st.session_state.emotion)
    elif  memory.page=="emotion_detection":
        processing()
    elif memory.page=="home":
        st.title(":musical_score: MoodMelody :musical_score:\n")
        st.write("##### :violin: Allow music to express your emotions!")
        st.divider()

        feedback_form()


        language_genres = {
                "Telugu": "tollywood",
                "Hindi": "bollywood",
                "Punjabi": "punjabi",
                "Tamil": "tamil",
                "Malayalam": "malayalam",
                "Kannada": "kannada",
                "Bengali": "bengali",
                "Gujarati": "gujarati",
                "Marathi": "marathi",
                "Bhojpuri": "bhojpuri",
                "English": "pop",  # General English pop
                "Rajasthani": "rajasthani",
                "Odia": "odia",
                "Assamese": "assamese"
            }
        genres=[i for i,j in language_genres.items()]

            # User selects a language

        st.subheader("Pick your preferred language of songs 	:world_map:")
        selected_language = st.selectbox("",genres,key="language",placeholder="click to select")
        st.divider()
        artist=[]
        names = []
        st.subheader(" Pick your favourite singers :male-singer: ")
        if selected_language:
            with st.spinner("searching for top 	:two::zero: artists in your preferred language"):
                genre = language_genres[f"{selected_language}"]
                memory.genre=genre
                results = sp.search(q=f'genre:"{memory.genre}"', type='artist', limit=30)
                meta_data = results['artists']['items']
                artists = {}
                for i in meta_data:
                    artists.update({f"{i['name']}": [f"{i['images'][2]['url']}", f"{i['popularity']}"]})

                fam_artists = dict(sorted(artists.items(), key=lambda item: item[1][1], reverse=True))

                cols=st.columns(4)

                count=0
                for row in range(6):
                    for col in range(4):

                         with(cols[col]):

                             name, url, = list(fam_artists.items())[count]
                             names.append(name)
                             reseponse=requests.get(url[0])
                             image=(Image.open(BytesIO(reseponse.content)))
                             st.image(image.resize((200,200)),caption="")
                             st.checkbox(f"{name}",key=name)
                             count+=1
            memory.names=names
            st.divider()
            for name in st.session_state.names:
                if st.session_state[f'{name}']:
                    artist.append(name)
            st.session_state.artists=artist
            st.info("Note:\n"
                    "Make sure that you have selected your preferences before clicking this button ")
            st.button(":camera: First let me see your mood :camera:", type="primary", on_click=emotion_detector)






