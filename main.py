import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="brexit ")

@bot.event
async def on_ready():
    print("brexit bot ready")

@bot.command()
async def brexit(ctx):
    await ctx.send("I agree")
    
@bot.group()
async def define(ctx):
    await ctx.send("Please choose something to define.")
    
@define.command()
async def boris_johnson(ctx):
    await ctx.send("A Poundland version of Donald Trump." \
                   "e.g If someone is seen to be copying someone else but in a worse manner," \
                   "you could say they are an absolute boris johnson")

@commands.command()
@commands.is_owner()
async def scream(ctx):
    for i in range(5):
        await ctx.send("AAAAAAAAAAAAAAAAAAAAAAAAAA!")
    
@commands.command(name="verytasty")
async def mmm(ctx):
    await ctx.send("reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee thats some good szechuan sauce ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")

bot.run("token")
