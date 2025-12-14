''' Temparary program for rooms
'''
import json

import sys
print(sys.path[0])


from program.extra_usefull.validation_for_inputs import valid_bool, valid_int
from program.npc.npc_list import npcs


def add_room(rooms):
    raise KeyError # some other data need to be passed
    try:
        general_data = read_json(FILENAME)
        data = fetch_data("rooms", general_data)
        print(data)
    except:
        print("rooms does not exist in JSON")

def create_room():
    x = "place holder"
    room = {
        "description" : x,
        "visited": False,

        "npc_active" :  False,
        "enemies_active" : False,
        "extra_function_active" : False,
            }
    
    room_name = input("Enter the name of the room:\n")
    npc_active = valid_bool("Are NPCs in this room?")
    if not npc_active:
        enemies_active = valid_bool("Are ENEMIES in this room?")
    extra_function_active = valid_bool("Does the room have any other extra functions?")

    if npc_active:
        room["npc_active"] = npc_active

        npc_names = list(npcs.keys())
        for i, name in enumerate(npc_names, start=1):
            print(f"{i}. {name}")
        
        selection = valid_int("Select which NPC will be present in the room")

        room["npc"] = npc_names[selection - 1]



    room["enemies_active"] = enemies_active
    room["extra_function_active"] = extra_function_active

if __name__ == "__main__":
    rooms = {}
    create_room()