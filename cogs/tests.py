from discord.ext import commands
import aiosqlite

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
        db = await aiosqlite.connect('anotherDiscordBot.db')
        premiumStatus = await db.execute("SELECT premiumStatus FROM premium WHERE userId = {}".format(userId))

        if premiumStatus == 1:
            await ctx.send('You are premium')
        else:
            await ctx.send('You are not premium')
        await db.close()

    @commands.command()
    async def economyStatus(self, ctx):
        """Test economyStatus command."""
        userId = ctx.author.id
        db = await aiosqlite.connect('anotherDiscordBot.db')
        cursor = await db.execute("SELECT economyStatus FROM economy WHERE userId = {}".format(userId))
        economyStatus = await cursor.fetchone()
        economyStatus = economyStatus[0]
        economyStatuString = str(economyStatus)
        await ctx.send(economyStatuString + '$')
        await db.close()

async def setup(bot):
    """Load the TestCog class."""
    await bot.add_cog(Tests(bot))
