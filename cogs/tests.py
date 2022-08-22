from discord.ext import commands
from db import DB

class Tests(commands.Cog):
    def __init__(self, bot):
        """Initialize the TestCog class."""
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Test command."""
        await ctx.send('pong')

    @commands.command()
    async def premiumStatus(self, ctx):
        """Test premiumStatus command."""
        userId = ctx.author.id
        guildId = ctx.guild.name.replace(' ', '')
        db = DB("anotherDiscordBot.db")
        premiumStatus = db.get_premium_status(guildId, userId)

        if premiumStatus == 1:
            await ctx.send('You are premium')
        else:
            await ctx.send('You are not premium')

    @commands.command()
    async def economyStatus(self, ctx):
        """Test economyStatus command."""
        userId = ctx.author.id
        guildId = ctx.guild.name.replace(' ', '')
        db = DB("anotherDiscordBot.db")
        economyStatus = db.get_economy_status(guildId, userId)
        economyStatuString = str(economyStatus)
        await ctx.send(economyStatuString + '$')

async def setup(bot):
    """Load the TestCog class."""
    await bot.add_cog(Tests(bot))
