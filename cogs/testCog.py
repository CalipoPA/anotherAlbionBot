import discord
from discord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, client):
        """Initialize the TestCog class."""
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        """Log the bot is logged and ready."""
        print(f'Bot logged on as {self.client.user}')

    @commands.command()
    async def ping(self, ctx):
        """Test command."""
        await ctx.send('pong')

    def cog_unload(self):
        """Log the bot is unloaded."""
        print('TestCog unloaded')

def setup(client):
    """Load the TestCog class."""
    client.add_cog(TestCog(client))
