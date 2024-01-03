import discord
import random
import music


if __name__ == '__main__':
   bot.run_discord_bot()
#    runs the bot

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(client)

