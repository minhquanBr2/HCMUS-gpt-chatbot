import openai
import time
import numpy as np
import config

openai.api_key = config.api_key
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
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    time.sleep(1)
    return response.choices[0].text.strip()

file_script = open("chatbot_script.txt", "r+")
file_train = open("chatbot_train.txt", "r+")
description = file_script.read() + file_train.read()
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
    

file_script.close()
file_train.close()

