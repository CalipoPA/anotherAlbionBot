# anotherDiscordBot
# author: @CalipoPA

import discord
from discord.ext import commands
from termcolor import colored
import os
from db import DB
import logging

# get environment variables
DISCORD_TOKEN = os.environ.get('TOKEN')

class anotherBot(commands.Bot):
    async def setup_hook(self) -> None:

        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await self.load_extension(f'cogs.{file[:-3]}')

def setup():
    print(colored('[+]', 'green'), colored('Starting bot...', 'white'))

    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    intents = discord.Intents.all()
    bot = anotherBot(intents=intents, command_prefix='!')
    bot.run(DISCORD_TOKEN)

setup()
