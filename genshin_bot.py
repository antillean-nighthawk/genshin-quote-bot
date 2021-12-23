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
        self.hello = random.choice(voice_lines[0])
        self.chat = random.choice(voice_lines[1])
        self.weather = random.choice(voice_lines[2])
        self.time = random.choice(voice_lines[3])
        self.about_self = random.choice(voice_lines[4])
        self.about_us = random.choice(voice_lines[5])
        self.vision = random.choice(voice_lines[6])
        self.share = random.choice(voice_lines[7])
        self.interesting_things = random.choice(voice_lines[8])
        self.about_others = random.choice(voice_lines[9])
        self.hobbies = random.choice(voice_lines[10])
        self.troubles = random.choice(voice_lines[11])
        self.food = random.choice(voice_lines[12])
        self.birthday = random.choice(voice_lines[13])
        self.ascension = random.choice(voice_lines[14])

def make_character(person):
    if person == 'hu-tao':
        character = Character(voice_lines.hu_tao_lines)
    elif person == 'kaeya':
        character = Character(voice_lines.kaeya_lines)
    elif person == 'albedo':
        character = Character(voice_lines.albedo_lines)
    elif person == 'venti':
        character = Character(voice_lines.venti_lines)
    elif person == 'rosaria':
        character = Character(voice_lines.rosaria_lines)
    elif person == 'klee':
        character = Character(voice_lines.klee_lines)
    elif person == 'kujou-sara':
        character = Character(voice_lines.kujou_sara_lines)
    elif person == 'raiden-shogun':
        character = Character(voice_lines.raiden_shogun_lines)

    return character

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))      

@bot.command()
async def say(ctx, person, line = None):
    character = make_character(person)
        
    if line == 'hello' or line == None:
        await ctx.send(character.hello)
    elif line == 'chat':
        await ctx.send(character.chat)
    elif line == 'weather':
        await ctx.send(character.weather)
    elif line == 'time':
        await ctx.send(character.time)
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