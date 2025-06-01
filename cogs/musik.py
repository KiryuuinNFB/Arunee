import discord
import yt_dlp as youtube_dl
import json
from discord.ext import commands

class musik(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.song_queue = []
        self.current_song = "เราไม่ได้เปิดอะไรนะ"
        self.loop_song = None

    async def skip_queue(self, ctx):
        try:
            if ctx.voice_client.is_playing():
                return
            else:
                if len(self.song_queue) > 0:
                    if self.loop_song == None:
                        await self.play_song(ctx, self.song_queue[0])
                        await ctx.send(f"กำลังเล่น {self.song_queue[0]} จากคิว")
                        self.song_queue.pop(0)
                    else:
                        await self.play_song(ctx, self.loop_song)
                elif len(self.song_queue) <= 0:
                    if self.loop_song == None:
                        await ctx.send("เพลงในคิวหมดละ")
                        self.current_song = "เราไม่ได้เปิดอะไรนะ"
                        return
                    else:
                        await self.play_song(ctx, self.loop_song)
                    
        except Exception as e: await ctx.send(f"เกิดข้อผิดพลาดที่มันแบบว่า {str(e)}")

    #ระบบเปิดเพลง
    async def play_song(self, ctx, url):
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn ' ,
        }
        YDL_OPTIONS = {
            'format': 'bestaudio/best',
            'quiet': True,
        }
        
        vc = ctx.voice_client
      
        try:
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                if 'formats' not in info or not info['formats']:
                    await ctx.send("หาฟอร์แมทเสียงไม่ได้อะ")
                    return
                

            with open("dumps.json", 'w', encoding='utf-8') as f:
                json.dump(info["formats"], f, ensure_ascii=False, indent=4)
            
            for formats in reversed(info['formats']):
                if formats["audio_ext"] == "mp4":
                    url2 = formats["url"]
                    break
          
            
                    

            #url2 = info['formats'][0]['url']
            print(f"Streaming URL: {url2}")
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            self.current_song = url
            vc.play(source,after=lambda e: self.client.loop.create_task(self.skip_queue(ctx)), bitrate=192)
        except Exception as e:
            await ctx.send(f"เกิดข้อผิดพลาดที่มันแบบว่า {str(e)}")

    #ระบบหาเพลง yt
    async def search_song(self, amount, song, get_url=False):
        info = await self.client.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio[ext=webm]/bestaudio[ext=m4a]/bestaudio", "quiet" : True,"noplaylist" : True}).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch"))
        if len(info["entries"]) == 0: return None

        return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    #join
    @commands.command(aliases=['j'])
    async def join(self, ctx):
        #คนพิมไม่อยุในห้องเสียง
        if ctx.author.voice is None:
            return await ctx.send("เข้าห้องเสียงด้วย ไม่งั้นชั้นจะเปิดเพลงให้เธอไม่ได้")
        #คนพิมอยุในห้องเสียง
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

        await ctx.author.voice.channel.connect()

    #leave
    @commands.command(aliases=['dis'])
    async def leave(self, ctx):
        if ctx.author.voice is None:
            return await ctx.send("ไม่")
        if ctx.voice_client is not None:
            self.song_queue.clear()
            return await ctx.voice_client.disconnect()
        
        await ctx.send("ชั้นไม่ได้อยุในห้องเสียง")

    #search
    @commands.command()
    async def search(self, ctx, *, song=None):
        if song is None: return await ctx.send("กรุณาใส่เพลง ไม่งั้นชั้นจะหาเพลงให้เธอไม่ได้")

        await ctx.send("รอแปป กำลังหาเพลงให้")
        
        info = await self.search_song(9, song)

        embed = discord.Embed(title=f"ที่เราหามาได้ทั้งหมดอะ", description="ตรงนี้ต้องเขียวป่าววะ ถ้าไม่เขียนแล้วโค้ดจะบักป่าววะ\n", colour=discord.Colour.from_rgb(255, 242, 128))

        amount = 0
        for entry in info["entries"]:
            embed.description += f"[{entry['title']}]({entry['webpage_url']})\n"
            amount += 1
        embed.set_footer(text=f"หามาให้ {amount} อัน")
        await ctx.send(embed=embed)

    #play
    @commands.command(aliases=['p'])
    async def play(self, ctx, *, song=None):
        #ไม่ใส่เพลง
        if song is None:
            return await ctx.send("กรุณาใส่เพลง ไม่งั้นชั้นจะเปิดเพลงให้เธอไม่ได้")
        
        #บอทไม่อยู่ในห้อง
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
                embed=discord.Embed(title="กรุณาใช้อย่างระมัดระวัง", description="เรายังมีปัญหาเรื่องนี้อยู่นะ\n1.บางเพลงเล่นแล้วคุณภาพต่ำ\n2.ใส่เพลย์ลิสต์ไม่ได้\n3.คิวเพลงยังใช้ร่วมกันทุกเซิฟเวอร์อยู่", color=0xe85d72)
                embed.set_author(name="อารุณี Production Model", url="https://bit.ly/3uzs80E", icon_url="https://media.discordapp.net/attachments/645528014691631105/1286258285502005311/Aru_Halo.webp?ex=66ed40e0&is=66ebef60&hm=8facb080907133dbc21e9858dde1d1be799fd1a27a77a297656b380e83710360&=&format=webp")
                embed.set_footer(text="ใช้แล้วเกิดปัญหาอะไรโปรดแจ้ง Kiryuuin")
                await ctx.send(embed=embed)
            else:
                return await ctx.send("กรุณาเข้าห้องเสียง ไม่งั้นชั้นจะเปิดเพลงให้เธอไม่ได้")

        #เพลงไม่ใช่ url
        if not ("youtube.com/watch?"in song or "https://youtu.be/"in song):
            await ctx.send("รอแปป กำลังหาเพลงให้")

            result = await self.search_song(1, song, get_url=True)
            #หาเพลงไม่เจอ
            if result is None:
                return await ctx.send("เราหาเพลงไม่เจออะ")

            song = result[0]

        if ctx.voice_client.is_playing():
            queue_len = len(self.song_queue)
            self.song_queue.append(song)
            return await ctx.send(f"เพิ่ม {song} ลงในคิวที่ {queue_len+1} เรียบร้อย")

        

        await self.play_song(ctx, song)
        await ctx.send(f"กำลังเล่น {song}")


    #queue
    @commands.command(aliases=['q'])
    async def queue(self, ctx):
        if len(self.song_queue) == 0:
            return await ctx.send("ในคิวไม่มีเพลง")

        embed = discord.Embed(title="คิวเพลง", description="", colour=discord.Colour.from_rgb(255, 132, 128))
        i = 1
        for url in self.song_queue:
            embed.description += f"{i}) {url}\n"
        
            i += 1

        embed.set_footer(text="บอทตัวนี้เป็นทรัพย์สินของ NFB PRODUCTION ละมั้ง")
        await ctx.send(embed=embed)

    #skip
    @commands.command(aliases=['fs'])
    async def skip(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("เรายังไม่ได้เปิดเพลงเลยนะ")

        if ctx.author.voice is None:
            return await ctx.send("เธอไม่ได้อยู่ในห้องเสียง")
        
        #ข้าม
        ctx.voice_client.stop()
        await ctx.send("ข้ามให้ละ")
    
    #pause
    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("pause ให้ละ")

    #resume
    @commands.command(aliases=['res'])
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("กำลังเล่นต่อ")

    #clear
    @commands.command(aliases=['cls'])
    async def clear(self, ctx):
        self.song_queue.clear()
        await ctx.send("clear ละ")

    #sp
    @commands.command(aliases=['sp'])
    async def pIay(self, ctx, *, song=None):
        #ไม่ใส่เพลง
        if song is None:
            return await ctx.send("กรุณาใส่เพลง ไม่งั้นชั้นจะเปิดเพลงให้เธอไม่ได้")
        #บอทไม่อยู่ในห้อง
        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()

        #เพลงไม่ใช่ url
        if not ("youtube.com/watch?"in song or "https://youtu.be/"in song):
            await ctx.send("รอแปป กำลังหาเพลงให้")

            result = await self.search_song(1, song, get_url=True)
            #หาเพลงไม่เจอ
            if result is None:
                return await ctx.send("เราหาเพลงไม่เจออะ")
            
            song = result[0]
            hehe ="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        
        if ctx.voice_client.source is not None:
            queue_len = len(self.song_queue)
            self.song_queue.append(hehe)
            return await ctx.send(f"เพิ่ม {song} ลงในคิวที่ {queue_len+1} เรียบร้อย")

        await self.play_song(ctx, hehe)
        await ctx.send(f"กำลังเล่น {song}")

    @commands.command(aliases=['crnt'])
    async def current(self, ctx):
        await ctx.send(self.current_song)
        
    @commands.command()
    async def loop(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("เราไม่ได้อยู่ในห้องเสียง")
        else:
            if self.loop_song == None:
                self.loop_song = self.current_song
                await ctx.send("เปิดลูปเพลงเรียบร้อย")
            else:
                self.loop_song = None
                await ctx.send("ปิดลูปเพลงละ")

async def setup(client):
    await client.add_cog(musik(client))