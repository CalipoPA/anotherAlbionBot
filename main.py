# anotherDiscordBot
# author: @CalipoPA

import discord
from discord.ext import commands
from termcolor import colored
import os
import logging
import aiosqlite

# get environment variables
DISCORD_TOKEN = os.environ.get('TOKEN')

class anotherBot(commands.Bot):
    async def setup_hook(self) -> None:

        # aiosqlite connection
        self.db = await aiosqlite.connect('anotherDiscordBot.db')
        self.db.row_factory = aiosqlite.Row

        # create tables if they don't exist
        await self.db.execute('''
        CREATE TABLE IF NOT EXISTS premium 
        (userId VARCHAR(255), premiumStatus VARCHAR(255))
        ''')
        await self.db.execute('''
        CREATE TABLE IF NOT EXISTS economy 
        (userId VARCHAR(255), economyStatus INT)
        ''')
        await self.db.commit()
        await self.db.close()

        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await self.load_extension(f'cogs.{file[:-3]}')

def setup():
    print(colored('[+]', 'yellow'), colored('Starting bot...', 'white'))

    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    intents = discord.Intents.all()
    bot = anotherBot(intents=intents, command_prefix='!')
    print(colored('[+]', 'green'), colored('Bot is ready!', 'white'))
    bot.run(DISCORD_TOKEN)

setup()
