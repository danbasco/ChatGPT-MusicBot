import discord
from discord.ext import commands
from ai import *

import datetime

class Fun(commands.Cog):
    
#init
    
    def __init__(self, client):
        self.client = client


    @commands.command(name="ai")
    async def _ai(self, ctx, *, text):

        resposta = open_ai(text)
        await ctx.reply(resposta)

        write(ctx.author, ctx.message, resposta, datetime.datetime.utcnow())


    @commands.command(name="fala", aliases=["say"])
    async def _fala(self, ctx, *, string):

        lista = ["everyone", "here", "@"]

        for item in lista:
            if item in string:
                return ...
            
        await ctx.send(str(string))
        

async def setup(client):
    await client.add_cog(Fun(client))