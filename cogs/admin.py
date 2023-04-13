
##This cog was made for organizing special commands for the bot, usually admin commands or other useful stuff that i dont include as AI commands or Music commands



import datetime

import discord
from discord.ext import commands


class Admin(commands.Cog):
    
#init
    
    def __init__(self, client):
        self.client = client


    #BOT INV


    @commands.command(name="invite", aliases=["convite"])
    async def _invite(self, ctx):

        embed = discord.Embed(
                title="`Invite`",
                description=f"",
                color=0xa8326d,
            )
        embed.add_field(name="", value= "Gostaria de adicionar a **Lil Rei** no seu servidor?\nIsso ficou fácil, basta clicar [aqui!](https://discord.com/api/oauth2/authorize?client_id=1080924319250661456&permissions=8&scope=applications.commands%20bot)")
        embed.set_image(url="https://cdn.discordapp.com/avatars/1080924319250661456/d824459f3f40dacac1357c1d4c00ceb3.png?size=2048")
        embed.set_footer(text= "Lil Rei • © Todos os direitos reservados.")
        await ctx.send(embed=embed)
        

async def setup(client):
    await client.add_cog(Admin(client))