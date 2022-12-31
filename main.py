# anotherAlbionBot
# author: @CalipoPA

import discord
from discord.ext import commands
from termcolor import colored
import os
import logging
import asyncpg
import asyncio

DISCORD_TOKEN = os.environ.get('TOKEN')

async def setupDatabase():
    try:
        conn = await asyncpg.connect(
            host = os.environ.get('HOST_DB'),
            database = os.environ.get('DATABASE'),
            user = os.environ.get('USER_DB'),
            password = os.environ.get('PASSWORD_DB')
        )
    except:
        print("Error to connect database")

    await conn.execute('''
        CREATE TABLE IF NOT EXISTS premium 
        (userId VARCHAR(255), premiumStatus VARCHAR(255))
        ''')
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS economy 
        (userId VARCHAR(255), economyStatus INT)
        ''')
    await conn.close()
    print(colored('[+]', 'green'), colored('Bot is ready!', 'white'))

class anotherBot(commands.Bot):
    async def setup_hook(self) -> None:
        
        await setupDatabase()

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
    bot.run(DISCORD_TOKEN)

asyncio.run(setup())
