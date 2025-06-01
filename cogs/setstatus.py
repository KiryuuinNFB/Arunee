import discord
from discord.ext import commands
from confidential import Kiryuuin

class setstatus(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setstatus(self, ctx, *, status):
        if ctx.author.id == Kiryuuin:
            await self.client.change_presence(status=discord.Status.idle,activity=discord.Game(status))
            await ctx.send(f"ตั้งสถานะเป็น {status} เรียบร้อย")
        else:
            await ctx.send("เธอไม่มีสิทธิ์ใช้คำสั่งนี้นะ")


async def setup(client):
    await client.add_cog(setstatus(client))