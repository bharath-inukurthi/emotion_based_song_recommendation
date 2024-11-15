from logging import exception
import streamlit as st
import numpy as np
from PIL import Image
import gspread as gs
from google.oauth2.service_account import Credentials
from my_secrets import sheet_id
from datetime import datetime
from deepface import DeepFace
from time import sleep

def preferences():
    st.session_state.page = 'home'
def song():
    st.session_state.page='song'

def feedback_form():

    #This feature of Feedback Collection into google sheets if disabled.
    #This can be used when developer have created a service account for google cloud console with googlesheets API.


    """ allow = ['https://www.googleapis.com/auth/spreadsheets']
credentials = Credentials.from_service_account_file("credentials.json", scopes=allow)
login = gs.authorize(credentials)
file = login.open_by_key(sheet_id)
working_sheet = file.sheet1"""

    st.sidebar.header("Feedback Form")

        # Email input
    email = st.sidebar.text_input("Email:", placeholder="Enter your email")

        # Feedback text area
    feedback = st.sidebar.text_area("Your Feedback:", placeholder="Type your feedback here")

    # Submit button
    if st.sidebar.button("Submit"):

        """if email and feedback:
            time_stamp = datetime.now().strftime("%H:%M:%S  %Y-%m-%d")
            working_sheet.append_row([email, feedback, time_stamp])
            st.sidebar.success("Thank you for your feedback!")
        else:
            st.sidebar.error("Please enter both email and feedback.")"""
        pass
    st.sidebar.divider()
    st.sidebar.info("If you are using MOBILE :iphone: we RECOMMEND you to switch to DESKTOP SITE in chrome settings ",icon="ℹ️")

def processing():

    feedback_form()
    st.sidebar.button(":scroll: Back to preferences :scroll:", type='primary', on_click=preferences,key='preference')
    st.title(":camera: First let me see your mood :camera:")
    image = st.camera_input("")

    if image:

        st.session_state.captured = True
        img = np.array(Image.open(image))



        try:
            results = DeepFace.analyze(
                img,
                actions=['emotion'],
                enforce_detection=False,detector_backend='yolov8'
            )
            emotion = results[0]['dominant_emotion']
            mapping = {
                'sad': 'Sad', 'happy': 'Happy', 'angry': 'Calm', 'fear': 'Calm',
                'neutral': 'Calm', 'disgust': 'Calm', 'surprise': 'Happy'
            }
            st.session_state.emotion=mapping[f'{emotion}']
            # Add emotion text to the image
            st.info(f"We noticed that your feeling {st.session_state.emotion}")
            place = st.empty()

            for i in range(5,-1,-1):
                place.success(f":notes: we will play melody of your {st.session_state.emotion}ness in {i}secs :notes:")
                sleep(1)

        except exception or BaseException as e:
            st.info(f"No face detected{e}")
            pass
        finally:
            song()
            st.rerun(scope="app")



