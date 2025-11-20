room_list=[] #Holds the room dictionaries.
loot_list=[] #Holds the loot dictionaries.
monster_list=[] #Holds the monster dictionaries.

"""Writes the entire list of rooms to the json file."""
def write_rooms(room_list): #For now has the list taken as an argument. Idk if that's what I'm supposed to do.
    import json
    jtext=json.dumps(room_list)
    with open("rooms.json","w") as f:
        f.write(jtext)

"""Writes the entire list of loot to the json file."""
def write_loot(loot_list): #For now has the list taken as an argument. Idk if that's what I'm supposed to do.
    import json
    jtext=json.dumps(loot_list)
    with open("loot.json","w") as f:
        f.write(jtext)

"""Writes the entire list of monsters to the json file."""
def write_monsters(monster_list): #For now has the list taken as an argument. Idk if that's what I'm supposed to do.
    import json
    jtext=json.dumps(monster_list)
    with open("monsters.json","w") as f:
        f.write(jtext)
