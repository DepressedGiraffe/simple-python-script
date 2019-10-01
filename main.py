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

@commands.command()
@commands.is_owner()
async def scream(ctx):
    for i in range(5):
        await ctx.send("AAAAAAAAAAAAAAAAAAAAAAAAAA!")
        
@bot.command()
async def reverse(ctx, *, text:str):
    await ctx.send(text[::-1])
    
@bot.command()
async def shout(ctx, *, text:str):
    await ctx.send(text.upper())
    
@bot.command()
async def novowels(ctx, text:str):
    vowels = {
        "a": "",
        "e": "",
        "i": "",
        "o": "",
        "u": ""
    }
    
    newtext = text.maketrans(vowels)
    await ctx.send(newtext)

@define.command()
async def boris_johnson(ctx):
    await ctx.send("A Poundland version of Donald Trump." \
                   "e.g If someone is seen to be copying someone else but in a worse manner," \
                   "you could say they are an absolute boris johnson")

@define.command()
async def brexit(ctx):
    await ctx.send("The act of telling everyone at a gathering (party, meeting ... etc.), that you are leaving, but actually staying.")

bot.run("token")
