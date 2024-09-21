# Import necessary libraries
import requests  # Used for making HTTP requests
import json  # Used for working with JSON data
import uuid

# Define constants for the script
CHUNK_SIZE = 1024  # Size of chunks to read/write at a time
XI_API_KEY = "sk_00e67c53a163ea22c6674d52f3b7997709c30cb97c3d69b5"  # Your API key for authentication
VOICE_ID = "LcfcDJNUP1GQjkzn1xUU"  # ID of the voice model to use
TEXT_TO_SPEAK = (
    "My name is Emily, I be your therapist today."  # Text you want to convert to speech
)
OUTPUT_PATH = "output.mp3"  # Path to save the output audio file

# Construct the URL for the Text-to-Speech API request
tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

# Set up headers for the API request, including the API key for authentication
headers = {"Accept": "application/json", "xi-api-key": XI_API_KEY}


# Set up the data payload for the API request, including the text and voice settings
def create_voice_message(message):
    msg_id = uuid.uuid4()
    TEXT_TO_SPEAK = message
    OUTPUT_PATH = f"{msg_id}.mp3"
    data = {
        "text": TEXT_TO_SPEAK,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True,
        },
    }

    # Make the POST request to the TTS API with headers and data, enabling streaming response
    response = requests.post(tts_url, headers=headers, json=data, stream=True)

    # Check if the request was successful
    if response.ok:
        # Open the output file in write-binary mode
        with open(OUTPUT_PATH, "wb") as f:
            # Read the response in chunks and write to the file
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                f.write(chunk)
        # Inform the user of success
        print("Audio stream saved successfully.")
        return msg_id
    else:
        # Print the error message if the request was not successful
        print(response.text)
