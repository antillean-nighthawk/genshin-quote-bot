import fandom

fandom.set_wiki("genshin-impact")

def get_character_names():
    page = fandom.page(title = "Characters")
    sec = page.section("Playable Characters")
    chars = sec.split()
    
    # filter out character names
    irrelevant = ['selection:', 'Icon', 'Name', 'Rarity', 'Element', 'Weapon', 'Region', 'Model', 'Type', 
    'Male', 'Female', 'Tall', 'Short', 'Medium', 'None', 'Playable', 'Characters', 'See', 'also:',
    'Characters/List', '53', 'match', 'the', 'category', 'Geo', 'Pyro', 'Cryo', 'Dendro', 'Hydro', 'Electro',
    'Anemo', 'Mondstadt', 'Liyue', 'Sumeru', 'Inazuma', 'Bow', 'Claymore', 'Catalyst', 'Sword', 'Polearm']
    other_chars = ['Aether:', 'MaleLumine:', 'Arataki', 'Itto', 'Hu', 'Tao', 'Kamisato', 'Ayato', 'Ayaka', 'Raiden', 'Shogun', 
    'Sangonomiya', 'Kokomi', 'Kuki', 'Shinobu', 'Yun', 'Jin', 'Snezhnaya', 'Kaedehara', 'Kazuha', 'Kujou', 'Sara',
    'Shikanoin', 'Heizou', 'Yae', 'Miko']
    remove = irrelevant + other_chars

    for r in remove:
        while r in chars:
            chars.remove(r)

    # add back 2-word names
    chars += ['Arataki Itto', 'Hu Tao', 'Kaedehara Kazuha', 'Kamisato Ayaka', 'Kamisato Ayato', 'Kujou Sara',
    'Kuki Shinobu', 'Raiden ShSogun', 'Sangonomiya Kokomi', 'Shikanoin Heizou', 'Yae Miko', 'Yun Jin']
    
    return chars

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

def find_name(character_name):
    names = get_character_names()

    if (character_name.lower() == "lumine") or (character_name.lower() == "aether"):
        character_name = "Traveler"

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