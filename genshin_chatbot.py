import os, random
import scraper
from dotenv import load_dotenv
import discord
from discord.ext import commands

# icons from https://genshin.gg/
# voice lines from https://genshin-impact.fandom.com/wiki/
# character info from https://en.wikipedia.org/wiki/List_of_Genshin_Impact_characters

# known issues: 
# some dialog lines aren't seperated by newlines (esp the traveler's)
# some character icons aren't displayed

load_dotenv()
intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)

character_info = scraper.get_character_info()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(aliases=['r', 'random'], help="Chat with a random character", brief="Sytax: $random")
async def _random(ctx):
    name = random.choice(scraper.get_character_names(character_info))
    lines = scraper.get_voice_lines(name)
    source = 'https://genshin-impact.fandom.com/wiki/' + name.replace(" ", "_") + '/Voice-Overs'
    embed = discord.Embed(description=random.choice(lines), color=discord.Color.blue())
    embed.set_author(name=name, url=source, icon_url=scraper.get_icon(name))
    await ctx.send(embed=embed)

@client.command(aliases=['c'], help="Chat with a specific character", brief="Sytax: $chat [character_name]")
async def chat(ctx, character_name):
    name = scraper.find_name(character_name, character_info)

    if name == "Not found":
        await ctx.send("That's not a character!")
    else:
        lines = scraper.get_voice_lines(name)
        source = 'https://genshin-impact.fandom.com/wiki/' + name.replace(" ", "_") + '/Voice-Overs'
        embed = discord.Embed(description=random.choice(lines), color=discord.Color.blue())
        embed.set_author(name=name, url=source, icon_url=scraper.get_icon(name))
        await ctx.send(embed=embed)

@client.command(aliases=['i'], help='View character icon', brief='Syntax: $icon [character_name]')
async def icon(ctx, character_name):
    name = scraper.find_name(character_name, character_info)

    if name == "Not found":
        await ctx.send("That's not a character!")
    else:
        embed = discord.Embed(title=name)
        embed.set_image(url=scraper.get_icon(name))
        await ctx.send(embed=embed)

@client.command(aliases=['w'], help='View character weapon', brief='Syntax: $weapon [character_name]')
async def weapon(ctx, character_name):
    name = scraper.find_name(character_name, character_info)
    source = "https://en.wikipedia.org/wiki/List_of_Genshin_Impact_characters"

    if name == "Not found":
        await ctx.send("That's not a character!")
    else:
        embed = discord.Embed(title=scraper.get_character_description(name, character_info, 4))
        embed.set_author(name=name, url=source, icon_url=scraper.get_icon(name))
        await ctx.send(embed=embed)

@client.command(aliases=['e'], help='View character element', brief='Syntax: $element [character_name]')
async def element(ctx, character_name):
    name = scraper.find_name(character_name, character_info)
    source = "https://en.wikipedia.org/wiki/List_of_Genshin_Impact_characters"

    if name == "Not found":
        await ctx.send("That's not a character!")
    else:
        embed = discord.Embed(title=scraper.get_character_description(name, character_info, 3))
        embed.set_author(name=name, url=source, icon_url=scraper.get_icon(name))
        await ctx.send(embed=embed)

@client.command(aliases=['n'], help='View character nationality', brief='Syntax: $nationality [character_name]')
async def nationality(ctx, character_name):
    name = scraper.find_name(character_name, character_info)
    source = "https://en.wikipedia.org/wiki/List_of_Genshin_Impact_characters"

    if name == "Not found":
        await ctx.send("That's not a character!")
    else:
        embed = discord.Embed(title=scraper.get_character_description(name, character_info, 5))
        embed.set_author(name=name, url=source, icon_url=scraper.get_icon(name))
        await ctx.send(embed=embed)

@client.command(aliases=['d'], help='View character description', brief='Syntax: $description [character_name]')
async def description(ctx, character_name):
    name = scraper.find_name(character_name, character_info)
    source = "https://en.wikipedia.org/wiki/List_of_Genshin_Impact_characters"

    if name == "Not found":
        await ctx.send("That's not a character!")
    else:
        embed = discord.Embed(title=scraper.get_character_description(name, character_info, 7))
        embed.set_author(name=name, url=source, icon_url=scraper.get_icon(name))
        await ctx.send(embed=embed)

client.run(os.getenv('TOKEN'))