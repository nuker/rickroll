from headers import *

class rick_cog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name='rick')
    async def test(self, ctx):
        await ctx.message.delete()
        await ctx.send("https://tinyurl.com/bdhwxm98")

async def setup(bot):
    await bot.add_cog(rick_cog(bot))
