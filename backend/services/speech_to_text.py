import requests
from services.preprocess_json import simplify_json
from services.gpt_service import gptresponse
def speech_to_text(text, audiofilepath):
    key = "K4C9%2BJHxKNv6rAZpg0mIuC4LUmAq8h%2Fss4zMommvligzrjk1d2jdWqRIUkMMCka6KtZaHY8hE8bVcqgFC6j4pf2%2FWia99z0gNG4nV14IOKyDy%2BKieBqyAlUbGKQHnsET"
    api_endpoint = "https://api.speechace.co"
    url = api_endpoint + "/api/scoring/text/v9/json"
    dialect = "en-us"
    user_id = "81ozow"

    url += "?" + "key=" + key + "&dialect=" + dialect + "&user_id=" + user_id

    payload = {"text": text}
    user_file_handle = open(audiofilepath, "rb")

    files = {"user_audio_file": user_file_handle}
    response = gptresponse(simplify_json(requests.post(url, data=payload, files=files)), text)
    
    return response


#speech_to_text("“Yes.”said Canine “I know exactly what’s wrong, The children are beginning to eat far too many sweets and are not looking after their teeth at all.” “I know…we can fix it!” Said Molar the wise one. She sounded quite excited by her grand idea.", "/Users/harsh/Documents/hackDavis-2024/test.mp3")