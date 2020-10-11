import discord
from discord.ext import commands

class TemplateBotCore(commands.Cog):

    def __init__(self, bot): 
        self.bot = bot

    @commands.command()
    async def hi(self, ctx):
        """Says Hi Back"""
        await ctx.send(f"{ctx.author.mention} Hello!!")


def setup(bot):
    bot.add_cog(TemplateBotCore(bot))