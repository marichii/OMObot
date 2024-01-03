import discord
from discord.ext import commands
import youtube_dl
import asyncio
import os
import time

voice_clients = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
ffmpeg_options = {'options': "-vn"}

# everything below is to get the bot running
TOKEN = 'MTExMzMyMjE2MTcwOTUxNDkxMw.G6_D1k.nFlsJlbkxgPjNEK070iaT9FDOV6GBquplPb140'
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Activated!')
hi_msgs = {"hi", "hey", "hello"}
lol_msgs = {"lol", "lmao", "lmfao"}
@client.event
async def on_message(msg):
    
    if msg.author != client.user:
        if msg.content.lower().startswith(tuple(hi_msgs)): 
            await msg.channel.send(f"Greetings, {msg.author.display_name}")
    if msg.author != client.user:
        if msg.content.lower().startswith("omo"): 
            await msg.channel.send(f"Greetings, {msg.author.display_name}")
    if msg.author != client.user:
        if msg.content.lower().startswith("?help"):
            await msg.channel.send(f"No.")
    
    
    if msg.author != client.user:
        if msg.content.lower().startswith(tuple(lol_msgs)):
            await msg.channel.send(f"hoo..haa...hooohoo")

    if msg.content.startswith("?play"):
        try: #creates the voice stream
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client #designates bot instance to single server
        except:
            print("error")

        try:
            url = msg.content.split()[1] #takes only the link

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False)) #creates the search point

            song = data['url'] #runs the link through data
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

            voice_clients[msg.guild.id].play(player)
        except Exception as err:
            print(err)
    if msg.content.startswith("?pause"):
        try: 
            voice_clients[msg.guild.id].pause()
        except Exception as err:
            print(err)
    if msg.content.startswith("?resume"):
        try: 
            voice_clients[msg.guild.id].resume()
        except Exception as err:
            print(err)
    if msg.content.startswith("?stop"):
        try: 
            voice_clients[msg.guild.id].stop()
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)

client.run(TOKEN)
