from discord.ext import commands
import aiosqlite

class Events(commands.Cog):
    def __init__(self, Bot) -> None:
        """Initialize the Events class."""
        self.get_guild = Bot.get_guild

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Event that triggers when the bot joins a guild."""
        db = await aiosqlite.connect('anotherDiscordBot.db')
        db.row_factory = aiosqlite.Row

        premiumStatus = False
        economyStatus = int(100)
        for member in guild.members:
            await db.execute("INSERT INTO economy (userId, economyStatus) VALUES ({}, {})".format(member.id, economyStatus))
            await db.execute("INSERT INTO premium (userId, premiumStatus) VALUES ({}, {})".format(member.id, premiumStatus))
        await db.commit()
        await db.close()

async def setup(bot):
    await bot.add_cog(Events(bot))