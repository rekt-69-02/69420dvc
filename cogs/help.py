import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        e = discord.Embed(title="Help", color=discord.Colour.yellow())
        e.add_field(name="setup", value="Setup a dynamic voice channel system (you can setup multiple ones).", inline=False)
        e.add_field(name="limit", value="Set the limit of the voice channel. Not entering a value makes it a one-person only vc.", inline=False)
        e.add_field(name="perm", value="Set the permission of the voice channel. You can enter multiple user names to add them once.", inline=False)
        e.add_field(name="name", value="Set the voice channel's name.", inline=False)
        await ctx.send(embed=e)

async def setup(bot):
    await bot.add_cog(Help(bot=bot))