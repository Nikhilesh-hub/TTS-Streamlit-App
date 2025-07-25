import streamlit as st
import io
import base64
from datetime import datetime
from gtts import gTTS
import os
import tempfile
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Set page configuration
st.set_page_config(
    page_title="Text to Speech Converter",
    page_icon="🔊",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    padding: 2rem;
}
.stTextArea textarea {
    height: 200px;
}
.download-button {
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# App title and description
st.title("Text to Speech Converter")
st.markdown("Convert your text to speech with customizable voice settings.")

# Text input area
text_input = st.text_area("Enter text to convert to speech", 
                         "Hello! Welcome to the Text to Speech converter app.")

# Voice settings
st.subheader("Voice Settings")

col1, col2 = st.columns(2)

with col1:
    # Language selection for gTTS
    language_options = {
        "English (US)": "en",
        "English (UK)": "en-gb",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Italian": "it",
        "Portuguese": "pt",
        "Russian": "ru",
        "Japanese": "ja",
        "Korean": "ko",
        "Chinese": "zh-CN"
    }
    
    selected_language = st.selectbox(
        "Select Language",
        options=list(language_options.keys()),
        index=0
    )

with col2:
    # Speech speed options
    speed_options = {
        "Very Slow": True,
        "Slow": True,
        "Normal": False,
        "Fast": False,
        "Very Fast": False
    }
    
    selected_speed = st.selectbox(
        "Select Speech Rate",
        options=list(speed_options.keys()),
        index=2,  # Default to Normal
        help="Controls the speech rate"
    )
    
    st.caption("Note: Very Slow and Slow use gTTS's slow mode. Normal, Fast, and Very Fast use standard mode.")
    
    # Additional options can be added here in the future

# Function to convert text to speech and return audio file
def text_to_speech(text, language, slow=False):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        temp_filename = fp.name
    
    # Use gTTS to convert text to speech
    # The 'slow' parameter is True for 'Very Slow' and 'Slow' options,
    # and False for 'Normal', 'Fast', and 'Very Fast' options
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save(temp_filename)
    
    # Read the saved file
    with open(temp_filename, 'rb') as f:
        audio_data = f.read()
    
    # Remove the temporary file
    os.unlink(temp_filename)
        
    return audio_data

# Convert button
if st.button("Convert to Speech"):
    if text_input.strip() == "":
        st.error("Please enter some text to convert.")
    else:
        with st.spinner("Converting text to speech..."):
            try:
                # Get language code from the selected language name
                language_code = language_options[selected_language]
                
                # Get slow parameter based on selected speed
                slow_param = speed_options[selected_speed]
                
                # Convert text to speech
                audio_data = text_to_speech(text_input, language_code, slow_param)
                
                # Generate a timestamp for the filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"speech_{timestamp}.mp3"
                
                # Create a download button for the audio
                st.audio(audio_data, format="audio/mp3")
                
                # Encode the audio data to base64 for download
                b64 = base64.b64encode(audio_data).decode()
                href = f'<a href="data:audio/mp3;base64,{b64}" download="{filename}" class="download-button">Download MP3 File</a>'
                st.markdown(href, unsafe_allow_html=True)
                
                st.success("Text converted to speech successfully!")
            except Exception as e:
                error_msg = f"Error converting text to speech: {str(e)}"
                logging.error(error_msg)
                st.error(f"An error occurred: {str(e)}")
                # You could add additional error handling here for production

# Footer
st.markdown("---")
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("Made with ❤️ using Streamlit and Google Text-to-Speech")
with col2:
    st.markdown("<a href='https://github.com/Nikhilesh-hub/TTS-Streamlit-App.git' target='_blank'>GitHub Repository</a>", unsafe_allow_html=True)
