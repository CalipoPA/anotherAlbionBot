from discord.ext import commands

class Tests(commands.Cog):
    def __init__(self, bot):
        """Initialize the TestCog class."""
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Test command."""
        await ctx.send('pong')

async def setup(bot):
    """Load the TestCog class."""
    await bot.add_cog(Tests(bot))
