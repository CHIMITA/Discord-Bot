import discord
from discord.ext.commands import Bot
import asyncio


bot = Bot(command_prefix=':',intents=discord.Intents.all())


token = "MTA5NjUwMjU1NTAxNTY2MzY3Ng.GhNyAD.9hHhOKcSWQ7dS3L9tjRx55UQl5PffeqEgP1QV4"

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
    


@bot.command()
async def on_msg(message):
    await message.reply('HI!')
    

bot.run(token)