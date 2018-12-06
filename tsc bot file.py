#importing

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
from discord import Game
import asyncio
import random

#defining client

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

#on message

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="I AM WORKING ON UPDATES"))
    print("By AJ")

#message events

@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, ":ping_pong: Pong <@%s>!" % (userID))
    if message.content.upper().startswith('!CLEAR'):
        tmp = await client.send_message(message.channel, 'Clearing messages... This may take a while. Be patient.')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
    if ('https://') in message.content:
        userID = message.author.id
        await client.send_message(message.channel, ":warning: Don't post links! <@%s>" % (userID))
        await client.delete_message(message)

#help command

@client.event
async def on_message(message):
    embed=discord.Embed(title="TSCBot's Commands", description="Here are TSCBot's commands, all of these are non case sensitive.", color=0xffff00)
    embed.add_field(name="!Ping", value="play ping pong with your friend! (who is the bot, right?)", inline=True)
    ###UNFINISHED
    
#bot's token

client.run("NTE2MDcwMjkyNjI4NDM5MDYw.DutDZg.oTqstnIPE5hGXYPcNM0mXqmS4X4")
