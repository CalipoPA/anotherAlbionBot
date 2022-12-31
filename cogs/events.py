from discord.ext import commands
import asyncpg
import os

async def connectDatabase():
    conn = await asyncpg.connect(
        host = os.environ.get('HOST_DB'),
        database = os.environ.get('DATABASE'),
        user = os.environ.get('USER_DB'),
        password = os.environ.get('PASSWORD_DB')
    )
    return conn

class Events(commands.Cog):
    def __init__(self, Bot) -> None:
        """Initialize the Events class."""
        self.bot = Bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Event that triggers when the bot joins a guild."""
        try:
            conn = await connectDatabase()
            premiumStatus = False
            economyStatus = int(100)
            for member in guild.members:
                await conn.execute("INSERT INTO economy (userId, economyStatus) VALUES ({}, {})".format(member.id, economyStatus))
                await conn.execute("INSERT INTO premium (userId, premiumStatus) VALUES ({}, {})".format(member.id, premiumStatus))
            await conn.close()
        except:
            print("Error on Database connection")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Event that triggers when a member joins the guild."""
        try:
            conn = await connectDatabase()
            premiumStatus = False
            economyStatus = int(100)
            await conn.execute("INSERT INTO economy (userId, economyStatus) VALUES ({}, {})".format(member.id, economyStatus))
            await conn.execute("INSERT INTO premium (userId, premiumStatus) VALUES ({}, {})".format(member.id, premiumStatus))
            await conn.close()
        except:
            print("Error on Database connection")


async def setup(bot):
    await bot.add_cog(Events(bot))