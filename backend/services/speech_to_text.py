import requests


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
    response = requests.post(url, data=payload, files=files)
    print(response.text)

    return response
