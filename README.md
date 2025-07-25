# Text to Speech Converter App

A simple Streamlit application that converts text to speech with customizable voice settings using Google's Text-to-Speech API.

## Features

- Convert text to speech
- Multiple language options (English US/UK, Spanish, French, German, Italian, Portuguese, Russian, Japanese, Korean, Chinese)
- Adjustable speech rate (Very Slow, Slow, Normal, Fast, Very Fast)
- Audio playback directly in the browser
- Download the generated audio as MP3

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Open your web browser and go to the URL displayed in the terminal (usually http://localhost:8501)
3. Enter the text you want to convert to speech
4. Adjust the voice settings as desired
5. Click the "Convert to Speech" button
6. Listen to the generated speech and download the MP3 file if needed

## Requirements

- Python 3.7 or higher
- Streamlit 1.23.0
- gTTS 2.3.2 (Google Text-to-Speech)

## Note

This app uses Google Text-to-Speech (gTTS), which requires an internet connection to function. The service supports multiple languages and provides high-quality speech synthesis.

## Deployment

### Streamlit Community Cloud (Recommended)

1. Push your code to a GitHub repository
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud)
3. Sign in with your GitHub account
4. Deploy your app by selecting your repository
5. Your app will be available at a public URL

### Alternative Deployment Options

- **Heroku**: Deploy using a Procfile and requirements.txt
- **Render**: Easy deployment with automatic builds from GitHub
- **Railway**: Simple deployment with GitHub integration
- **Self-hosting**: Deploy on your own server or cloud instance