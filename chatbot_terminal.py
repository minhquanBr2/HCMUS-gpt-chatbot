import openai
import time
import numpy as np

openai.api_key = "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"
prompts = [
    "Hi, how can I help you today?",
    "What brings you here?",
    "How can I assist you?"
]


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    time.sleep(1)
    return response.choices[0].text.strip()

file_description = open("chatbot_description.txt", "r+")
description = file_description.read()
prompt = ""
history = ""
prompt_id = int(np.random.randint((len(prompts))))
prompt = prompts[prompt_id]
print("Brend: " + prompts[prompt_id])


while True:
    user_input = input("User: ")
    history += "\nUser: " + user_input
    prompt = description + "\n" + history + "\Brend: "
    response = generate_response(prompt)
    print("Brend: ", response)
    history += response
    
 
