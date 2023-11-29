import openai
import os
import sys 

openai.api_key = os.environ['OPENAI_API_KEY']

target_language = input("What language do you want tranlate to?\n>".strip())
text = input("What do you want to translate?\n>".strip())


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": f"translate the following English text into {target_language}"},
        {"role" : "user", "content": text}
    ]
)
print(response['choices'][0]['message']['content'].strip())
