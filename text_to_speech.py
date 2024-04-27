import os
import uuid

from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

# ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_API_KEY = "56fed7fcb4574f5b9de5b1d11535f194"
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def text_to_speech_file(text: str, filename) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="4akuk2vRYPQlh6t4cOFN",  # Adam pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # uncomment the line below to play the audio back
    # play(response)

    # Generating a unique file name for the output MP3 file
    #save_file_path = f"{uuid.uuid4()}.mp3"
    save_file_path = f"{filename}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path



text_to_speech_file("The animals came from far and near across the dusty African plain. They came on padding paws and pounding hooves and flapping wings.", 'teacher')

text_to_speech_file("Each beast, from the tiniest ant to the largest elephant, made its way to Pride Rock. For that was the home of the Lion King, and this was a special day in the pride Lands.", 'student')


