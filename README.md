
# 🎵 Emotion-Based Song Recommender
An intelligent application that curates song recommendations based on users' emotions and preferences. Using emotion detection, the app analyzes user input to understand their mood, then sends a query to the Spotify API with the user's preferred language and artists for a truly personalized playlist.

### 🚀 Key Features:

**Emotion Detection:**  Recognizes emotions such as happiness, sadness, and calmness, tailoring music to suit the user’s mood.

**Spotify Integration:** Connects with Spotify API to deliver music recommendations based on language and artist preferences.

**Customizable Preferences:** Users can specify preferred music languages and artists for a unique experience.

**Streamlit Interface:** User-friendly interface built with Streamlit for smooth interaction.

**Feedback Form:** Integrated form for user feedback to continually improve recommendations.







## Integrating Your API Key

Follow steps mentioned  from the [spotify-setup-guide.md](https://github.com/bharath-inukurthi/emotion_based_song_recommendation/blob/main/emotion_based_song_recomendation/spotify-setup-guide.md) file in repository to get spotify Credentials.

Replace values of below given variables in [my_secrets.py](emotion_based_song_recomendation/my_secrets.py) file in repository
```bash
  SPOTIFY_CLIENT_ID = 'your spotify client id'
  SPOTIFY_CLIENT_SECRET = 'your spotify client secret'
```

**NOTE** : For maintaining developers privacy the functionality of feedback form is in __commented__ state as the functionality requires developers google cloud console project's service account credentials




# Create a virtual environment

I recommend you to create a virtual environment to avoid compatibilty issues

### macOS/Linux (using Python's venv):
```bash
  python3.12 -m venv myenv
```

```bash
  source myenv/bin/activate
```
### Windows (using Python's venv):

```bash
  python3.12 -m venv myenv
```

```bash
  myenv\Scripts\activate
```


### Using conda:
```bash
  conda create -n myenv python=3.12
```



```bash
  conda activate myenv
```





# Run Locally

Clone the project



```bash
  git clone https://github.com/bharath-inukurthi/emotion_based_song_recommendation.git
```

Go to the project directory

```bash
  cd emotion_based_song_recommendation/emotion_based_song_recomendation
```

Install dependencies

```bash
  pip install -r requirements
```

Start the WebAPP

```bash
  streamlit run homepage.py
```


## Feedback

If you have any feedback, please reach out to us at bharathinukurthi1@gmail.com


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://everything-about-bharath.webflow.io/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bharath-kumar-inukurthi/)


