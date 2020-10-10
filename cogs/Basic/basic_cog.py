import discord
from discord.ext import commands

class BasicCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is up and running!!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(self.client.latency)