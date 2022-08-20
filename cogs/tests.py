from discord.ext import commands

class Tests(commands.Cog):
    def __init__(self, client):
        """Initialize the TestCog class."""
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        """Test command."""
        await ctx.send('pong')

async def setup(client):
    """Load the TestCog class."""
    await client.add_cog(Tests(client))
