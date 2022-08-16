# anotherDiscordBot
# author: @CalipoPA

from dataclasses import fields
import discord
from discord.ext import commands
from termcolor import colored
from db import DB
import logging
import os

# set up environment variables
TOKEN = os.environ.get('TOKEN')
if TOKEN is None:
    print(colored('TOKEN not found in environment variables', 'red'))
else:
    print(colored('Loading Cogs...', 'yellow'))

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
        print(colored(f'{file[:-3]} Loaded!', 'green'))

# bot event for start db on new guild
@bot.event
async def on_guild_join(guild):

    # delete spacing string
    guildName = guild.name.replace(' ', '')
    db = DB("bot.db")
    db.create_table(guildName)

    guild = bot.get_guild(guild.id)
    premiumStatus = False
    economyStatus = int(100)
    for member in guild.members:
        db.insert_data(guildName, member.id, premiumStatus, economyStatus)


# run bot
bot.run(TOKEN)
