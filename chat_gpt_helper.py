import openai

openai.api_key = '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'
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


