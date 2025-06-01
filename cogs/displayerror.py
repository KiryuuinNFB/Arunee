from discord.ext import commands

class listener(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    #anti error
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(f'เกิดข้อผิดพลาดที่มันแบบว่า {error}')


async def setup(client):
    await client.add_cog(listener(client))