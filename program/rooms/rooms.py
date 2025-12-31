''' Temparary program for rooms
'''

from random import choice
import json

try:

    from program.read_write_json.read_json import read_json
    from program.read_write_json.write_json import update_room
    from program.extra_usefull.validation_for_inputs import valid_bool, valid_int
    from program.npc.npc_list import npcs

except:
    print("Call the program by typing")
    print("python -m program.rooms.rooms\nin the Terminal")
    raise Exception(
        "Stopped the code on purpose"
    )


def create_room():
    '''
    f: create_room()
    takes no parameters
    returns: simple room template that is ready to be added to JSON

    create_room:
        - name
        - description
        - visited (room_state)
        - npc_active
        - npc (The name of the npc present IF npc_active)
        - enemies_active
        - enemies (The type of enemies in the room)
        - enemies_count
        - exta_functon [True/False] (Used so main can check if there are extra functions that the room should preform)
        - connections (Door: N, S, E, W)
    '''
    room_name = input("Enter the name of the room:\n")
    author_name = input("Enter the author's name for this room:\n (enter your name)\n")

    room = {
        "_meta" : {
            "author" : author_name
        },
        "name" : room_name,
        "description" : "PLACE HOLDER",
        "visited": False,

        "npc_active" :  False,
        "enemies_active" : False,
        "extra_function_active" : False,

        "connections" : {} # It will count connections in this order:
        # North, South, East, West
            }
    
    npc_active = valid_bool("Are NPCs in this room?")
    if not npc_active:
        enemies_active = valid_bool("Are ENEMIES in this room?")
    extra_function_active = valid_bool("Does the room have any other extra functions?")

    # Connections for the room
    connect_north = valid_bool("Does this room have a connection at North?")
    connect_south = valid_bool("Does this room have a connection at South?")
    connect_east = valid_bool("Does this room have a connection at East?")
    connect_west = valid_bool("Does this room have a connection at West?")

    connections = {"north":connect_north, "south":connect_south, "east":connect_east, "west":connect_west}

    room["connections"] = connections


    # This block selects the npc in the room; if present
    if npc_active:
        room["npc_active"] = npc_active

        npc_names = list(npcs.keys())
        for i, name in enumerate(npc_names, start=1):
            print(f"{i}. {name}")
        
        selection = valid_int("Select which NPC will be present in the room")

        room["npc"] = npc_names[selection - 1]


    room["enemies_active"] = enemies_active
    room["extra_function_active"] = extra_function_active
    return room

def add_desc(room, description):
    '''Takes in a room and a description and updates the room to have that description.
    Rooms can have multiple descriptions
    Descriptions are numbered. Will automatically make the new description the next number.'''
    desc_num = -1
    new_desc_num = 0
    count = 0
    while desc_num<new_desc_num:
        desc_num = new_desc_num
        count = count + 1
        desc = f"description{count}"
        if desc in room:
            new_desc_num = count
        
    new_desc_num=new_desc_num+1
    desc=f"description{new_desc_num}"
    room[desc]=description
    update_room(room)


def choose_room():
    '''
    Chooses a room from the database and returns it

    f: functionality reserved for the running of the game
    THIS FUNCTION EXISTS FOR THE GAME NOT TO BE CALLED DIRECTLY

    comment: currently chooses a room at random
    '''
    data = read_json("database.json")
    rooms = data["rooms"]

    len_rooms = len(rooms)
    choose_room = choice(list(rooms.keys()))
    return choose_room

if __name__ == "__main__":
    rooms = {}
    room = create_room()

    # just re-names the room for the purpose of easier access later
    room_name = room["name"]
    rooms[room_name] = room

    print(room)
    
    # >>> Then add the room to the database




# Code for adding additional descriptions
'''
data=read_json("database.json")
room=data["rooms"]["basement"]
add_desc(room, "The floorboards creak softly as you move.")
'''