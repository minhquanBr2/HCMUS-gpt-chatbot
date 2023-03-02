import chatbot_helper as gpt
import discord
import config

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

client.run(config.discord_key)




