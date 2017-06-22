import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!")
var = bot.get_channel("327183009235075084")

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print("----------------------")

@bot.command()
async def test():
    await bot.say("Hello!")


@bot.command()
async def joinv():
    await bot.join_voice_channel(id(var))

bot.run("MzI3MTM5MDMzNTAxMjcwMDE2.DCw_hw.kHvl6E8reHjnA1VTLeA0bxEWR2s")




