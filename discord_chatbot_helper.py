import openai
import config

openai.api_key = config.api_key
model_engine = 'text-davinci-003'

def getResponse(user_prompt):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=user_prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1.5
    )
    response = completion.choices[0].text
    return response


