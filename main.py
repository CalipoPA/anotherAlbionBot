# anotherDiscordBot
# author: @CalipoPA

import discord
from discord.ext import commands
import logging
import os

# set up environment variables
TOKEN = os.environ.get('TOKEN')
if TOKEN is None:
    print('TOKEN not found')
else:
    print('TOKEN found')

# set up intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.messages = True
intents.guilds = True
intents.voice_states = True
intents.bans = True
intents.emojis = True
intents.webhooks = True
intents.reactions = True

# set up logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# set up bot
prefix = '!'
bot = commands.Bot(command_prefix=prefix, intents=intents)

for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')
        print(f'Cog {file[:-3]} loaded')

# run bot
bot.run(TOKEN)
