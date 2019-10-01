import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="brexit ")

@bot.event
async def on_ready():
    print("brexit bot ready")

@bot.command()
async def brexit(ctx):
    await ctx.send("I agree")
    
@bot.command()
async def uwu(ctx):
    await ctx.send("0w0")

bot.run("token")
