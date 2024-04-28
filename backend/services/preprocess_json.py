import json
null = None
# Sample JSON data from your API

def simplify_json(data):
    print(data)
    words = data['text_score']['word_score_list']
    # Calculate the average quality score of all words
    total_quality_score = sum(word['quality_score'] for word in words)
    average_quality_score = total_quality_score / len(words)

    simplified_data = []

    for word_info in words:
        if word_info['quality_score'] < average_quality_score and len(word_info['word']) >= 4:
            word_entry = {
                'word': word_info['word'],
                'context': {
                    'previous_word': None,  # Update these based on your data's sequence
                    'next_word': None
                },
                'phonetics': []
            }

            for phone_info in word_info.get('phone_score_list', []):
                if phone_info['sound_most_like'] and phone_info['sound_most_like'] != phone_info['phone']:
                    phonetic_entry = {
                        'actual_phonetic': phone_info['phone'],
                        'almost_sounds_like_phonetic': phone_info['sound_most_like'],
                        'stress_level': phone_info.get('stress_level'),
                        'predicted_stress_level': phone_info.get('predicted_stress_level')
                    }
                    word_entry['phonetics'].append(phonetic_entry)

            # Add context
            word_index = words.index(word_info)
            if word_index > 0:
                word_entry['context']['previous_word'] = words[word_index - 1]['word']
            if word_index < len(words) - 1:
                word_entry['context']['next_word'] = words[word_index + 1]['word']

            simplified_data.append(word_entry)

    return json.dumps(simplified_data,indent = 4)


