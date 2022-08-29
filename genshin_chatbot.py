import os, random
import scraper
from dotenv import load_dotenv
import discord
from discord.ext import commands

# icons from https://genshin.gg/
# voice lines from https://genshin-impact.fandom.com/wiki/

load_dotenv()
intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(aliases=['r', 'random'], help="Chat with a random character", brief="sytax: $random")
async def _random(ctx):
    name = random.choice(scraper.get_character_names())
    lines = scraper.get_voice_lines(name)
    source = 'https://genshin-impact.fandom.com/wiki/' + name.replace(" ", "_") + '/Voice-Overs'
    embed = discord.Embed(description=random.choice(lines), color=discord.Color.blue())
    embed.set_author(name=name, url=source, icon_url=scraper.get_icon(name))
    await ctx.send(embed=embed)

@client.command(aliases=['c'], help="Chat with a specific character", brief="sytax: $chat [character_name]")
async def chat(ctx, character_name):
    name = scraper.find_name(character_name)

    if name == "Not found":
        await ctx.send("That's not a character!")
    else:
        lines = scraper.get_voice_lines(name)
        source = 'https://genshin-impact.fandom.com/wiki/' + name.replace(" ", "_") + '/Voice-Overs'
        embed = discord.Embed(description=random.choice(lines), color=discord.Color.blue())
        embed.set_author(name=name, url=source, icon_url=scraper.get_icon(name))
        await ctx.send(embed=embed)

@client.command(aliases=['i'], help='View character icon', brief='syntax: $icon [character_name]')
async def icon(ctx, character_name):
    name = scraper.find_name(character_name)

    if name == "Not found":
        await ctx.send("That's not a character!")
    else:
        embed = discord.Embed(title=name)
        embed.set_image(url=scraper.get_icon(name))
        await ctx.send(embed=embed)

client.run(os.getenv('TOKEN'))