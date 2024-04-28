import os
import uuid

from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

# ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_API_KEY = "56fed7fcb4574f5b9de5b1d11535f194"
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def text_to_speech_file(text: str) -> str:
    
    response = client.text_to_speech.convert(
        voice_id="4akuk2vRYPQlh6t4cOFN",
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2", 
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )
    save_file_path = f"tts_output_{os.urandom(12).hex()}.mp3"

    #save_file_path = f"{filename}.mp3"

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    return save_file_path



#text_to_speech_file("The animals came from far and near across the dusty African plain. They came on padding paws and pounding hooves and flapping wings.", 'teacher')

#text_to_speech_file("Each beast, from the tiniest ant to the largest elephant, made its way to Pride Rock. For that was the home of the Lion King, and this was a special day in the pride Lands.", 'student')

#text_to_speech_file("Sure thing! Let's focus on the longer words to really hone your pronunciation. You're making great strides, so let's keep up the fantastic work! Canine: You're almost there! Try to make the 'a' sound like in 'cat,' and for the 'i,' imagine you're happy, saying it like 'i-e.' This will really help get that clear pronunciation. Teeth: A little tricky, but I know you can do it! Put your tongue just between your teeth and let a bit of air through for the 'th' sound. Say it like 't-e-th.' You're doing wonderfully with these words! Every little bit of practice is making you better, and I'm so proud of you for trying so hard. Keep practicing, and you'll see how much smoother it gets! You're doing an amazing job!",'sophia_response_to_student')
