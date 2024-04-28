from openai import OpenAI
import os

# Assuming you have already set up the OpenAI client as shown in your previous message
#client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
client = OpenAI(api_key='sk-proj-eBd63BQmZ86UAWgJYOF2T3BlbkFJtVkmcq7C1hj85xTcm7BQ')

def compare_sentences(sentence1, sentence2):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or the latest suitable model
            temperature=0.5,  # Adjust temperature based on desired creativity
            max_tokens=250,
            
            messages=[
                {"role": "system", "content": "You are a mother who is very nurturing and caring. You are teaching your child how to read senteces in english correctly and correcting the mistakes of wrongly pronounced words."},
                {"role": "user", "content": f"Reference: {sentence1}"},
                {"role": "user", "content": f"Spoken: {sentence2}"},
                {"role": "system", "content": "Answer like a mother. Correct the wrongly spoken words slowly."}
            ]
        )
        # Extracting just the text response from the assistant's last message
        last_message = response.choices[0].message.content
        return {"result": last_message}
    except Exception as e:
        return {"error": str(e)}
