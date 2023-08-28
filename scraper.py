import fandom, requests
from bs4 import BeautifulSoup

def scrape_wikipedia():
    character_info = []
    response = requests.get(url="https://en.wikipedia.org/wiki/List_of_Genshin_Impact_characters")
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr')

    for row in rows[1:-4]:
        info = [d.text.rstrip() for d in row.find_all('td')]
        if info:
            character_info.append(info)

    # combine traveler entries
    character_info[0][0] = "Aether/Lumine/Traveler"
    character_info[0][3] += character_info[1][1]
    character_info.pop(1)

    return character_info

# format names from user input
def find_name(character_name, character_info):
    names = []
    for character in character_info:
        if character:
            names.append(character[0])

    if character_name.lower() in "aether/lumine/traveler": return "Traveler"
    result = [i for i in names if character_name.lower() in i.lower()]

    if len(result) > 1:
        for name in result:
            word = name.split(" ")
            for w in word:
                if w.lower() == character_name.lower():
                    return name
    return result[0]

def get_character_description(name, character_info, col):
    for character in character_info:
        if character:
            if name.lower() == character[0].lower():
                return character[col]

def set_lang(language):
    if language in ["chn", "chinese", "c"]:
        return "/Chinese"
    elif language in ["kr", "korean", "k"]:
        return "/Korean"
    elif language in ["jp", "japanese", "j"]:
        return "/Japanese"
    else: # defaults to english
        return ""

def get_voice_lines(name, path):
    fandom.set_wiki("genshin-impact")
    page = fandom.page("{}/Voice-Overs{}".format(name, path))
    story = page.section("Story")
    if name == "Traveler": # traveler only has a few combat lines
        story = page.section("Combat")
    lines = story.split('\n')

    lines = lines[2:] # remove table header
    for i in range(len(lines)): # remove sound files
        try: index = lines[i].rindex(".ogg") + 5
        except: index = 0
        lines[i] = lines[i][index:]
        if name == "Fischl": # newlines for Fischl/Oz dialogue
            lines[i] = lines[i].replace(name+':', '\n'+name+':')
            lines[i] = lines[i].replace("Oz:", "\nOz:")
    return [x for x in lines if x] # clean null elements

def get_icon(character_name):
    last_names_only = ["Arataki Itto", "Kamisato Ayaka", "Kamisato Ayato", 
                       "Sangonomiya Kokomi", "Shikanoin Heizou", "Kaedehara Kazuha"]
    
    if character_name in last_names_only:
        first, last = character_name.split(' ')
        return f'https://rerollcdn.com/GENSHIN/Characters/1/{last}.png'
    elif character_name == "Raiden Shogun":
        return 'https://rerollcdn.com/GENSHIN/Characters/1/Raiden.png'
    elif character_name == "Aether/Lumine/Traveler": # elements are all the same image
        return 'https://rerollcdn.com/GENSHIN/Characters/1/Traveler%20(Anemo).png'
    else:
        percent_encoded = character_name.replace(" ", "%20")
        return f'https://rerollcdn.com/GENSHIN/Characters/1/{percent_encoded}.png'