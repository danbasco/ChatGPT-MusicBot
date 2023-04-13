#IMPORT
import asyncio
import datetime
import os

import discord
import pomice
from discord.ext import commands
from dotenv import load_dotenv

from ai import *

import openai


#.env files

load_dotenv()
    
TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_T = os.getenv("OPENAI")
OWNER_ID = int(os.getenv("OWNER_ID"))
APP_ID = int(os.getenv("APP_ID"))





class LilRei(commands.Bot):
    def __init__(self):
        
        super().__init__(
            command_prefix='!', #bot prefix
            help_command=None, 
            case_insensitive=True, 
            intents=discord.Intents.all(), 
            owner_id=OWNER_ID,
            application_id =APP_ID)

    async def on_ready(self):
        
        await self.wait_until_ready()
        await self.cogs["Music"].start_nodes()
                      
#status

        status = "Lil Rei | Trabalhando novamente..." #Set this as your discord bot status

        activity = discord.Game(name= status, type= 3)
        await client.change_presence(status=discord.Status.online, activity=activity)

        print("Bot está pronto")


client = LilRei() #the bot client


##EVENTS


@client.event
async def on_connect():
    print(f" Connected to Discord (latency: {client.latency*1000:,.0f} ms).")


@client.event
async def on_resumed():
    print("Bot resumed.")


@client.event
async def on_disconnect():
    print("Bot disconnected.")



@client.event

#respond if someone pings the bot!

async def on_message(message):
    
    if message.author.bot:
        return

    if isinstance(message.channel, discord.DMChannel):
        
        resposta = open_ai(str(message.content))
        await message.channel.send(resposta)

        write(message.author, message.content, resposta, datetime.datetime.utcnow())

    if client.user.mentioned_in(message):
        if "@" not in message.content.lower():
            return ...

        elif ("everyone" or "here" ) in message.content.lower():
            return ...

        else:
            await message.channel.send(f"O meu prefixo padrão é `!`") #Change the ! for the bot prefix
    else:
        await client.process_commands(message)


if __name__ == "__main__":

    #load the cogs method

    async def load_extensions():
        for files in os.listdir("./cogs"):
            if files.endswith(".py"):
                await client.load_extension(f"cogs.{files[:-3]}")
                print(f"Cog {files} carregada!")


    #main func to load the bot


    async def main():

        openai.api_key = OPENAI_T #your OpenAI API key, you can get this on the site

        await load_extensions()
    
        await client.start(TOKEN, reconnect=True)


    asyncio.run(main())
