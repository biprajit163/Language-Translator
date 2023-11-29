import openai
import os
import sys 

openai.api_key = os.environ['OPENAI_API_KEY']

text = "Hey how are you, what did you do today? I saw a beautiful sunset in the park."
target_language = "portuguese"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": f"translate the following English text into {target_language}"},
        {"role" : "user", "content": text}
    ]
)
print(response['choices'][0]['message']['content'].strip())
