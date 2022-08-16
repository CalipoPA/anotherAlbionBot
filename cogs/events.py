from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        """Initialize the Events class."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """on_ready event function"""
        print(f'Ready!')
        print(f'Logged in as ---->', self.bot.user,)
        print(f'ID:', self.bot.user.id)

    @commands.Cog.listener()
    async def on_message(self, message):
        """Listening for messages"""
        pass

def setup(bot):
    bot.add_cog(Events(bot))