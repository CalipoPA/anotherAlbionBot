from discord.ext import commands
from db import DB


class Events(commands.Cog):
    def __init__(self, Bot) -> None:
        """Initialize the Events class."""
        self.get_guild = Bot.get_guild

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Event that triggers when the bot joins a guild."""
        guildName = guild.name.replace(' ', '')
        db = DB("anotherDiscordBot.db")
        db.create_table(guildName)
        guild = self.get_guild(guild.id)
        premiumStatus = False
        economyStatus = int(100)
        for member in guild.members:
            db.insert_data(guildName, member.id, premiumStatus, economyStatus)


async def setup(bot):
    await bot.add_cog(Events(bot))