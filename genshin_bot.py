import discord
import os
import voice_lines
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
bot = commands.Bot(command_prefix='$')

class Character:
    def __init__(self, voice_lines):
        self.hello = voice_lines[0]
        self.chat = random.choice(voice_lines[1])
        self.rain = [2]
        self.thunder = [3]
        self.snw = [4]
        self.wind = random.choice(voice_lines[5])
        self.morning = voice_lines[6]
        self.afternoon = voice_lines[7]
        self.evening = voice_lines[8]
        self.night = voice_lines[9]
        self.about_self = random.choice(voice_lines[10])
        self.about_us = random.choice(voice_lines[11])
        self.vision = voice_lines[12]
        self.share = voice_lines[13]
        self.interesting_things = voice_lines[14]
        self.about_others = random.choice(voice_lines[15])
        self.hobbies = voice_lines[16]
        self.troubles = voice_lines[17]
        self.food = random.choice(voice_lines[18])
        self.birthday = voice_lines[19]
        self.ascension = random.choice(voice_lines[20])

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))      

@bot.command()
async def say(ctx, person, line = None):
    if person == 'hutao':
        character = Character(voice_lines.hu_tao_lines)
        
    if line == 'hello' or line == None:
        await ctx.send(character.hello)
    elif line == 'chat':
        await ctx.send(character.chat)
    elif line == 'rain':
        await ctx.send(character.rain)
    elif line == 'thunder':
        await ctx.send(character.thunder)
    elif line == 'snow':
        await ctx.send(character.snow)
    elif line == 'wind':
        await ctx.send(character.wind)
    elif line == 'morning':
        await ctx.send(character.morning)
    elif line == 'afternoon':
        await ctx.send(character.afternoon)
    elif line == 'evening':
        await ctx.send(character.evening)
    elif line == 'night':
        await ctx.send(character.night)
    elif line == 'about-character':
        await ctx.send(character.about_self)
    elif line == 'about-us':
        await ctx.send(character.about_us)
    elif line == 'about-others':
        await ctx.send(character.about_others)
    elif line == 'vision':
        await ctx.send(character.vision)
    elif line == 'share':
        await ctx.send(character.share)
    elif line == 'interesting-things':
        await ctx.send(character.interesting_things)
    elif line == 'hobbies':
        await ctx.send(character.hobbies)
    elif line == 'troubles':
        await ctx.send(character.troubles)
    elif line == 'food':
        await ctx.send(character.food)
    elif line == 'birthday':
        await ctx.send(character.birthday)
    elif line == 'ascension':
        await ctx.send(character.ascension)

bot.run(os.getenv('TOKEN'))
