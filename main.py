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
async def kick(ctx, member:discord.Member):
    await ctx.guild.kick(member, reason="kicked!")
    await ctx.send(f"{member.name} has been kicked from the server!")

@bot.command()
async def ban(ctx, member:discord.Member):
    await ctx.guild.ban(member, reason="banned!")
    await ctx.send(f"{member.name} has been banned from the server!")
    
@bot.command()
async def nick(ctx, member:discord.Member, *, nick:str):
    await member.edit(nick=nick)
    await ctx.send(f"Changed {member.name}'s nickname to {nick}")
    
@bot.command()
async def hackban(ctx, member_id:int):
    member = discord.Object(id=member_id)
    await ctx.guild.ban(member, reason="hackbanned!")
    await ctx.send(f"User with ID: {str(member_id)} has been banned from the server!")

bot.run("token")
