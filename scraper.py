import fandom
import requests
from bs4 import BeautifulSoup

fandom.set_wiki("genshin-impact")

def get_character_info():
    response = requests.get(url="https://en.wikipedia.org/wiki/List_of_Genshin_Impact_characters")
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr')

    character_info = []

    for row in rows:
        info = [d.text.rstrip() for d in row.find_all('td')]
        character_info.append(info)

    return character_info

def get_character_names(character_info):
    names = []

    for character in character_info:
        if character:
            names.append(character[0])

    names.append("Traveler")

    return names

def get_character_description(name, character_info, col):
    for character in character_info:
        if character:
            if name.lower() == character[0].lower():
                return character[col]

def get_voice_lines(name):
    path = "{}/Voice-Overs".format(name)
    page = fandom.page(path)
    story = page.section("Story")
    lines = story.split('\n')

    # remove junk
    lines.pop(0)
    lines.pop(0)

    # clean up lines
    for i in range(len(lines)):
        try:
            index = lines[i].rindex(".ogg") + 5
        except:
            index = 0

        lines[i] = lines[i][index:]

        if name == "Traveler":
            lines[i] = lines[i].replace("TitleDetails", "")
            lines[i] = lines[i].replace("AetherLumine", "")
            lines[i] = lines[i].replace("???", "")

    
    return lines

def get_icon(character_name):
    if character_name != "Traveler":
        icon_link = 'https://rerollcdn.com/GENSHIN/Characters/' + character_name.replace(" ", "%20") + '.png'
    else:
        icon_link = 'https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Anemo).png'

    return icon_link

def find_name(character_name, character_info):
    names = get_character_names(character_info)

    if (character_name.lower() == "lumine") or (character_name.lower() == "aether"):
        return "Traveler"

    result = [i for i in names if character_name.lower() in i.lower()]

    if not result:
        return "Not found"
    elif len(result) > 1:
        for name in result:
            word = name.split(" ")
            for w in word:
                if w.lower() == character_name.lower():
                    return name
    else:
        return result[0]