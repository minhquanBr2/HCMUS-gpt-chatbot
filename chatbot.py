import chat_gpt_helper as gpt
import discord

greetings = ['hello', 'hi', 'yo', 'sup']
greetings = tuple(greetings)

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith(greetings):
        print(message.content)
        await message.channel.send('Hola')
    else:
        print(message.content)
        response = gpt.getResponse(message.content)
        await message.channel.send(response)

client.run('MTA3OTU4NjQ0NzcwODkxNzc3MQ.GES9FX.cXfAGvXSUz2A-y_2YnL7-aNY4-va8fFToyGCew')




