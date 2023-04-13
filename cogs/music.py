
#This cog is not ready yet :)


import re

import discord
import pomice
from discord.ext import commands
from pomice import Player, Queue, events
from dotenv import load_dotenv
import os

URL_REG = re.compile(r'https?://(?:www\.)?.+')

class NoVoiceChannel(commands.CommandError):
    pass

class NoMusicSpecified(commands.CommandError):
    pass



class Music(commands.Cog):
    
#init
    
    def __init__(self, client):
        self.client = client
        self.pomice = pomice.NodePool()
        self.queue = Queue()

 
 #nodes

   


    async def start_nodes(self):
        print("Starting Nodes...")

         #SPOTIFY SECRET --> 

        load_dotenv()
        SPT_ID = os.getenv("SPOTIFY_ID")
        SPT_SECRET = os.getenv("SPOTIFY_SECRET")

        #loading the pomice node
        await self.pomice.create_node(bot=self.client, host="127.0.0.1",port=2333, identifier='MAIN', password="youshallnotpass", spotify_client_id=SPT_ID, spotify_client_secret= SPT_SECRET)
        print("Lavalink carregado com sucesso")


    
#commands



    @commands.command(name='join', aliases=['connect'])
    async def _join(self, ctx):
        
        try:
            channel = ctx.author.voice.channel
            
            await channel.connect(cls=pomice.Player)
            await ctx.reply("Bot conectado com sucesso!")
        except:
            raise NoVoiceChannel


    @commands.command(name="disconnect", aliases=["leave"])
    async def _disconnect(self, ctx):
        await ctx.author.voice.channel.disconnect()



    @commands.command(name='play', aliases = ["tocar", "p"])
    async def _play(self, ctx, *, search: str = None):

        if search is None:
            raise NoMusicSpecified

        else:    
            
            player = ctx.voice_client        
            results = await player.get_tracks(query=f'{search}')

            try:
                queue_orp = player.is_playing
                print(queue_orp)
                if queue_orp == False:
                    print("Primeira musica")
                    await player.play(track=results[0])

                else:
                    try:
                        print("Adicionando a fila")
                        self.queue.put(item=results[0])


                    except Exception as o:
                        print(o)
            except Exception as v:
                print(v)
            embed = discord.Embed(
                title=" `✅` | Adicionado à fila",
                description=f"Tocando agora...\n\n {results[0]}",
                color=0xa8326d,
            )
            await ctx.send(embed=embed)
            
    
    @commands.command(name="queue", aliases = ["q", "fila"])
    async def _queue(self, ctx):
        queue = self.queue.get_queue()
        print(queue)
        await ctx.send("teste")
        await ctx.send(f"{queue}")


    @commands.Cog.listener()
    async def on_command_error(self, ctx, exc):
            
             
        if isinstance(exc, NoVoiceChannel):
            await ctx.reply("`❌` | **Você precisa estar em um canal de voz para executar esse comando!**")
        if isinstance(exc, NoMusicSpecified):
            await ctx.reply("`❌` | **Nenhuma música foi especificada!**")
    
    #on testing 
    @commands.Cog.listener()
    async def on_pomice_track_end(self, player):
        print("debug")
        #track = self.queue.get()
        #await player.play(track)


async def setup(client):
    await client.add_cog(Music(client))

