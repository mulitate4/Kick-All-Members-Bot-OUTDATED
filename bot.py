import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = ""

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def test(ctx):
    await ctx.send("bruh moment")

@bot.command(pass_context=True)
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def kickall(ctx):
    guild = ctx.message.guild
    users = ctx.message.guild.members

    for user in users:
        print(user)
        try:
            await user.kick()
            print(user+"kicked")
        except:
            continue

bot.run(TOKEN, reconnect=True)
