import discord
from discord.ext import commands
from confidential import Kiryuuin

class help(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    def me(ctx):
        return ctx.author.id == Kiryuuin
    
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="คำสั่งทั่วไป", description="prefix 1.", color=0xe85d72)
        embed.set_author(name="อารุณี Production Model", url="https://bit.ly/3uzs80E", icon_url="https://media.discordapp.net/attachments/645528014691631105/1286258285502005311/Aru_Halo.webp?ex=66ed40e0&is=66ebef60&hm=8facb080907133dbc21e9858dde1d1be799fd1a27a77a297656b380e83710360&=&format=webp")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/645528014691631105/1286258907236270151/aru-haruka-and-hiyoris-anxiety-archive-v0-seg3zpk8a1ja1.webp?ex=66ed4175&is=66ebeff5&hm=c167409dded5918b96ca2d204f46a73ad06dd7215a02c6f5ab6f575f57ccefc1&=&format=webp")
        embed.add_field(name="1.help", value="ไม่ต้องบอกก็รู้", inline=True)
        embed.add_field(name="1.p /play {เพลง}", value="เปิดเพลง", inline=True)
        embed.add_field(name="1.join /j", value="เข้าห้องเสียง", inline=True)
        embed.add_field(name="1.search {เพลง}", value="แสดงผล Search จาก Youtube", inline=True)
        embed.add_field(name="1.clear /cls", value="ลบเพลงในคิวทั้งหมด", inline=True)
        embed.add_field(name="1.pause", value="หยุดเพลงชั่วคราว", inline=True)
        embed.add_field(name="1.resume /res", value="เปิดเพลงต่อหลัง Pause", inline=True)
        embed.add_field(name="1.disconnect /dis", value="ออกจากห้องเสียง", inline=True)
        embed.add_field(name="1.queue /q", value="ดูคิวเพลง",inline=True)
        embed.add_field(name="1.skip /fs", value="ข้ามเพลง", inline=True)
        embed.add_field(name="1.current /crnt", value="ดูเพลงที่กำลังเล่นอยู่ตอนนี้", inline=True)
        embed.add_field(name="1.loop", value="เปิด/ปิด ลูปเพลงที่กำลังเล่นอยู่", inline=True)
        embed.add_field(name="1.sp", value="(deprecated do not use)", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def adminhelp(self, ctx):
        embed=discord.Embed(title="คำสั่งแอดมิน", description="prefix 1.", color=0xfff280)
        embed.set_author(name="อารุณี Production Model", url="https://bit.ly/3uzs80E", icon_url="https://media.discordapp.net/attachments/645528014691631105/1286258285502005311/Aru_Halo.webp?ex=66ed40e0&is=66ebef60&hm=8facb080907133dbc21e9858dde1d1be799fd1a27a77a297656b380e83710360&=&format=webp")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/645528014691631105/1286258907236270151/aru-haruka-and-hiyoris-anxiety-archive-v0-seg3zpk8a1ja1.webp?ex=66ed4175&is=66ebeff5&hm=c167409dded5918b96ca2d204f46a73ad06dd7215a02c6f5ab6f575f57ccefc1&=&format=webp")
        embed.add_field(name="1.load {ext}", value="load extension", inline=True)
        embed.add_field(name="1.unload {ext}", value="unload entension", inline=True)
        embed.add_field(name="1.reload {ext}", value="reload extension", inline=True)
        embed.add_field(name="1.dm {user ID} {ข้อความ}", value="ส่งข้อความส่วนตัว", inline=True)
        embed.add_field(name="1.setstatus {status}", value="ตั้งค่าสถานะ", inline=True)
        embed.set_footer(text="คำสั่งแอดมินไม่ให้ใช้น๊จ๊ :>>>>>>>>")
        await ctx.send(embed=embed)

    @commands.command()
    async def test(self, ctx):
        embed=discord.Embed(title="กรุณาใช้อย่างระมัดระวัง", description="เรายังมีปัญหาเรื่องนี้อยู่นะ\n1.บางเพลงเล่นแล้วคุณภาพต่ำ\n2.บางเพลงเล่นแล้วไม่มีเสียง\n3.ใส่เพลย์ลิสต์ไม่ได้\n4.คิวเพลงยังใช้ร่วมกันทุกเซิฟเวอร์อยู่", color=0xe85d72)
        embed.set_author(name="อารุณี Production Model", url="https://bit.ly/3uzs80E", icon_url="https://media.discordapp.net/attachments/645528014691631105/1286258285502005311/Aru_Halo.webp?ex=66ed40e0&is=66ebef60&hm=8facb080907133dbc21e9858dde1d1be799fd1a27a77a297656b380e83710360&=&format=webp")
        embed.set_footer(text="ใช้แล้วเกิดปัญหาอะไรโปรดแจ้ง Kiryuuin")
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(help(client))