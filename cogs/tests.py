from discord.ext import commands


class Tests(commands.Cog):
    def __init__(self, client):
        """Initialize the TestCog class."""
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        """Test command."""
        await ctx.send('pong')

def setup(client):
    """Load the TestCog class."""
    client.add_cog(Tests(client))
