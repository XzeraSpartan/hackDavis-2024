import os
import requests

def compare_sentences(sentence1, sentence2):
    api_key = os.getenv('OPENAI_API_KEY')
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        "model": "text-davinci-003",
        "prompt": f"Please compare these two sentences for pronunciation accuracy:\n\nReference: {sentence1}\nSpoken: {sentence2}\n",
        "temperature": 0.5,
        "max_tokens": 150
    }
    response = requests.post('https://api.openai.com/v1/engines/text-davinci-003/completions', json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to connect to OpenAI API"}
