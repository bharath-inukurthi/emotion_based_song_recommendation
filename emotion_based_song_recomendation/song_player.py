from time import sleep
import streamlit as st

def query(sp,mood,offset=0):
    if mood=='Happy' and st.session_state.artists:
        query = f'genre:"{st.session_state.genre}" AND artist:"{st.session_state.artists[0]}"'

    else:
        query = f'genre:"{st.session_state.genre}"'


    results = sp.search(q=query, type='track', limit=50,offset=offset)
    tracks = results['tracks']['items']
    categorize(sp,mood,tracks,offset)
def categorize(sp,mood,tracks,offset):
    with st.spinner("analyzing song tracks for you..."):
        found=0
        for track in tracks:
            audio_features = sp.audio_features([track['id']])[0]
            sleep(0.1)
            mood1=''
            valence = audio_features['valence']
            energy = audio_features['energy']
            danceability = audio_features['danceability']

            if valence > 0.45 and danceability > 0.45:
                mood1= 'Happy'

            elif valence <= 0.3 and danceability <=0.45 :
                mood1= 'Sad'

            elif valence > 0.5 and energy < 0.4:
                mood1= 'Calm'

            if mood==mood1:
                get_song(track)
                found=1
                break
    if found==0:
            query(sp,mood,offset+50)

def get_song(track):
        # Get a random song and display its info
    if track:
        st.write(f"**Title:** {track['name']}")
        st.write(f"**Artist:** {', '.join([artist['name'] for artist in track['artists']])}")
        st.write(f"**Album:** {track['album']['name']}")
        st.image(track['album']['images'][0]['url'])  # Album cover image

            # Provide a link to play the song
        st.markdown(f"[Listen on Spotify](https://open.spotify.com/track/{track['id']})")

            # Play the preview URL (if available)
        if track['preview_url']:
            st.audio(track['preview_url'], format='audio/mp3')
        else:
            st.write("No preview available for this track.")
    else:
        st.write("No tracks found.")

