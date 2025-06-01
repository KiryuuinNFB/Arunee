import discord
import os
from discord.ext import commands
import asyncio
from confidential import Kiryuuin, bot_token

client = commands.Bot(command_prefix = commands.when_mentioned_or('1.'), intents = discord.Intents.all())

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('Kerbal Space Program'))
    print('อารุณี Production Model พร้อมใช้งาน')

def me(ctx):
    return ctx.author.id == Kiryuuin

#load cogs
@client.command()
async def load(ctx, extension):
    if ctx.author.id == Kiryuuin:
        await client.load_extension(f'cogs.{extension}')
        await ctx.send("Load เรียบร้อย")
    else:
        await ctx.send("เธอไม่มีสิทธิ์ใช้คำสั่งนี้นะ")

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == Kiryuuin:
        await client.unload_extension(f'cogs.{extension}')
        await ctx.send("Unload เรียบร้อย")
    else:
        await ctx.send("เธอไม่มีสิทธิ์ใช้คำสั่งนี้นะ")

@client.command()
async def reload(ctx, extension):
    if ctx.author.id == Kiryuuin:
        await client.reload_extension(f'cogs.{extension}')
        await ctx.send("Reload เรียบร้อย")
    else:
        await ctx.send("เธอไม่มีสิทธิ์ใช้คำสั่งนี้นะ")

@client.command()
async def dm(ctx, user: discord.User, *, msg):
    if ctx.author.id == Kiryuuin:
        await ctx.send("ส่งละ")
        await user.send(f'{msg}')
    else:
        await ctx.send("เธอไม่มีสิทธิ์ใช้คำสั่งนี้นะ")

@client.command()
async def send(ctx, channel: discord.TextChannel, *, msg):
    if ctx.author.id == Kiryuuin:
        await ctx.send("ส่งละ")
        await channel.send(f'{msg}')
    else:
        await ctx.send("เธอไม่มีสิทธิ์ใช้คำสั่งนี้นะ")
        
@client.command()
async def say(ctx, *, msg):
    if ctx.author.id == Kiryuuin:
        await ctx.message.delete()
        await ctx.send(msg)
    else:
        await ctx.send("เธอไม่มีสิทธิ์ใช้คำสั่งนี้นะ")

"""
for filename in os.listdir('./cogs'):       
    if filename.endswith('.py'):
        client.add_cog(f'cogs.{filename[:-3]}')
"""
async def load_all():
    await client.load_extension("cogs.displayerror")
    await client.load_extension("cogs.musik")
    await client.load_extension("cogs.help")
    await client.load_extension("cogs.setstatus")

asyncio.run(load_all())

client.run(bot_token)