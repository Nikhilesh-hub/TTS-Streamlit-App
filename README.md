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

- Python 3.10 or higher (Python 3.10.12 recommended for deployment)
- Streamlit 1.23.0
- gTTS 2.3.2 (Google Text-to-Speech)
- Pillow 9.5.0
- NumPy 1.20.0 or higher
- Pandas 1.3.0 or higher

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

## Troubleshooting

### Deployment Issues

- **Pillow Installation Failures**: If you encounter errors with Pillow installation during deployment, ensure you're using a compatible Python version (3.10.x recommended) and that Pillow is explicitly listed in requirements.txt.

- **Dependency Conflicts**: Some newer Python versions (like 3.13.x) may have compatibility issues with certain packages. If you encounter build errors, try specifying Python 3.10.12 in your runtime.txt file.

- **Memory Errors**: If you encounter memory errors during deployment, try reducing the size of your dependencies or upgrading to a higher tier on your hosting platform.

### Local Development Issues

- **Audio Not Playing**: Ensure your browser supports HTML5 audio playback.

- **gTTS API Errors**: If you encounter errors with the Google TTS API, check your internet connection and verify that the API is accessible from your location.
