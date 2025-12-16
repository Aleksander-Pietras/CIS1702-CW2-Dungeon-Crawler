''' Temparary program for rooms
'''
import json

try:
    from program.extra_usefull.validation_for_inputs import valid_bool, valid_int
    from program.npc.npc_list import npcs

except:
    print("Call the program by typing")
    print("python -m program.rooms.rooms\nin the Terminal")
    raise Exception(
        "Stoped the code on purpose"
    )

def add_room(rooms):
    raise NotImplementedError # some other data need to be passed
    try:
        general_data = read_json(FILENAME)
        data = fetch_data("rooms", general_data)
        print(data)
    except:
        print("rooms does not exist in JSON")

def create_room():
    room_name = input("Enter the name of the room:\n")

    room = {
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

if __name__ == "__main__":
    rooms = {}
    room = create_room()
    room_name = room["name"]
    rooms[room_name] = room

    print(room)