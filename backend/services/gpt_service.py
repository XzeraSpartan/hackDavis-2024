from openai import OpenAI
import os

# Assuming you have already set up the OpenAI client as shown in your previous message
#client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
client = OpenAI(api_key='sk-proj-eBd63BQmZ86UAWgJYOF2T3BlbkFJtVkmcq7C1hj85xTcm7BQ')

def gptresponse(data, text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or the latest suitable model
            temperature=0.5,  # Adjust temperature based on desired creativity
            max_tokens=250,
            
            messages=[
                {"role": "system", "content": "You are a mother who is very nurturing and caring. You are teaching your child how to read senteces in english correctly and correcting the mistakes of wrongly pronounced words. You are given a sentense and JSON full of information on how the word is pronounced. Ignore the simple words. Focus on words that are hard to pronouce by 5 year olds"},
                {"role": "user", "content": f"Reference: {data}"},
                {"role": "user", "content": f"sentence: {text}"},
                {"role": "system", "content": "Correct the wrongly spoken words slowly and sweetly with love. Ignore simple words. Correct only complicated words."}
            ]
        )
        # Extracting just the text response from the assistant's last message
        last_message = response.choices[0].message.content
        print(last_message)
        return {"result": last_message}
    except Exception as e:
        return {"error": str(e)}
