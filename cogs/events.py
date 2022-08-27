from discord.ext import commands
import aiosqlite

class Events(commands.Cog):
    def __init__(self, Bot) -> None:
        """Initialize the Events class."""
        self.bot = Bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Event that triggers when the bot joins a guild."""
        db = await aiosqlite.connect('anotherDiscordBot.db')

        premiumStatus = False
        economyStatus = int(100)
        for member in guild.members:
            await db.execute("INSERT INTO economy (userId, economyStatus) VALUES ({}, {})".format(member.id, economyStatus))
            await db.execute("INSERT INTO premium (userId, premiumStatus) VALUES ({}, {})".format(member.id, premiumStatus))
        await db.commit()
        await db.close()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Event that triggers when a member joins the guild."""
        db = await aiosqlite.connect('anotherDiscordBot.db')

        premiumStatus = False
        economyStatus = int(100)
        await db.execute("INSERT INTO economy (userId, economyStatus) VALUES ({}, {})".format(member.id, economyStatus))
        await db.execute("INSERT INTO premium (userId, premiumStatus) VALUES ({}, {})".format(member.id, premiumStatus))
        await db.commit()
        await db.close()

async def setup(bot):
    await bot.add_cog(Events(bot))