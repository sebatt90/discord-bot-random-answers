import asyncio
import discord
import json
import random

settings = json.load(open("./settings.json"))
client = discord.Client()

PREFIX = '!'


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Game(name="insert name of desired game activity or remove this line"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    file = open("./assets/commands.json")
    commands = json.load(file)

    for command in commands["commands"]:
        if message.content.startswith(PREFIX+command["command"]):
            l = len(command["answers"])
            r = random.randrange(0,l)
            await message.channel.send(command["answers"][r])
    
    file.close()

client.run(settings["token"])

