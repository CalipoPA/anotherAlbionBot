from discord.ext import commands
import time

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def time(self, ctx):
        t = time.gmtime()
        utc = time.strftime("%H:%M:%S", t)
        await ctx.send("**:alarm_clock: " + utc + " UTC**")

async def setup(bot):
    await bot.add_cog(Utils(bot))