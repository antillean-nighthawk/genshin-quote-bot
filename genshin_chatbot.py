import os, random, scraper
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
client = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

# basic info about characters
character_info = scraper.scrape_wikipedia()
async def detail(ctx, character_name, col):
    name = scraper.find_name(character_name, character_info)
    wikipedia = "https://en.wikipedia.org/wiki/List_of_Genshin_Impact_characters"

    if name == "Not found":
        await ctx.send("That's not a character!")
    else:
        embed = discord.Embed(title=scraper.get_character_description(name, character_info, col))
        embed.set_author(name=name, url=wikipedia, icon_url=scraper.get_icon(name))
        await ctx.send(embed=embed)

@client.command(aliases=['w'], help='View character weapon', brief='Syntax: $weapon [character_name]')
async def weapon(ctx, character_name):
    await detail(ctx, character_name, 2)

@client.command(aliases=['e'], help='View character element', brief='Syntax: $element [character_name]')
async def element(ctx, character_name):
    await detail(ctx, character_name, 1)

@client.command(aliases=['d'], help='View character description', brief='Syntax: $description [character_name]')
async def description(ctx, character_name):
    await detail(ctx, character_name, 4)

# chat commands
@client.command(aliases=['c'], help="Chat with a specific character", brief="Sytax: $chat [character_name]")
async def chat(ctx, character_name, language="eng"):
    try:
        if character_name in ["random", "r", "?"]:
            name = random.choice(character_info)[0]
        else:
            name = scraper.find_name(character_name, character_info)
    except:
        await ctx.send("That's not a character!")

    lines = scraper.get_voice_lines(name, scraper.set_lang(language))
    source = f'https://genshin-impact.fandom.com/wiki/{name.replace(" ", "_")}/Voice-Overs'
    embed = discord.Embed(description=random.choice(lines), color=discord.Color.blue())
    embed.set_author(name=name, url=source, icon_url=scraper.get_icon(name))
    await ctx.send(embed=embed)

@client.command(aliases=['r', 'random'], help="Chat with a random character", brief="Sytax: $random")
async def _random(ctx, language="eng"):
    await chat(ctx, "random", language)

@client.command(aliases=['i'], help='View character icon', brief='Syntax: $icon [character_name]')
async def icon(ctx, character_name):
    name = scraper.find_name(character_name, character_info)

    if name == "Not found":
        await ctx.send("That's not a character!")
    else:
        embed = discord.Embed(title=name)
        embed.set_image(url=scraper.get_icon(name))
        embed.set_author(url="https://genshin.gg/")
        await ctx.send(embed=embed)

# todo: help commands
client.run(os.getenv('APIKEY'))