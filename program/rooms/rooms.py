''' Temparary program for rooms
'''

from random import choice
from random import random
from random import randint
import random
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
    description = input("Please enter a description for this room:\n")

    room = {
        "_meta" : {
            "author" : author_name
        },
        "name" : room_name,
        "description" : description,
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
    else:
        enemies_active = False
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

def add_desc(room):
    '''Takes in a room and a description and updates the room to have that description.
    Rooms can have multiple descriptions
    Descriptions are numbered. Will automatically make the new description the next number.'''
    description=input(f"Please enter the new description for the {room["name"]}.")
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

def choose_random_description(room: dict):
    '''
    Chooses a description from the database and returns it
    '''
    descriptions = []
    for desc in room.keys():
        if "description" in desc:
            descriptions.append(room[desc])

    print(choice(descriptions))

def choose_room(rooms: dict):
    '''
    Chooses a room from the database and returns it

    f: functionality reserved for the running of the game
    THIS FUNCTION EXISTS FOR THE GAME NOT TO BE CALLED DIRECTLY

    comment: currently chooses a room at random
    '''

    choose_room = choice(list(rooms.keys()))
    return choose_room

def decide_on_directions(room: dict):
    ''' Display and allow player to chooses which direction to travel to

    parameters: room_data: dict

    returns: users choosen direction
    '''
    connections = room["connections"]
    valid_connections = []

    for direction, is_open in connections.items():
        if is_open:
            valid_connections.append(direction)

    while True:
        try:
            print("The room has doors facing:", end="")
            for con in valid_connections:
                print(f", {con}", end="")

            print("")

            choosen_direction = input(f"Which door do you wish to walk through?\n").lower()

            valid_choices = ["north", "south", "east", "west"]
            if choosen_direction in valid_choices:
                print("You have moved")
                return choosen_direction
            
            else:
                print("Incorrect input")

        except:
            pass

        
def empty_room():
    """ Displays text to say the same thing in different ways.
    """
    rand_text=random.randint(0,2)
    if rand_text==0:
        print("The are no enemies in this room.")
    elif rand_text==1:
        print("You feel calm. Your instincts tell you this room is safe.")
    elif rand_text==2:
        print("This room is eerily quiet. There's no monsters here.")

def choose_next_room(rooms_data, visited_rooms, direction_choice): #Will infinite loop if every room has been visited.
    room_not_found = True
    chosen_key = "Start Room"

    while room_not_found == True:
        room_not_found = False #Assumes found until proven otherwise
        index=random.randint(0,len(rooms_data)-1)
        count=0
        for key in rooms_data:
            if count == index:
                chosen_key = key
            count=count+1
        
        if chosen_key in visited_rooms: #If generated room has already been visited:
            room_not_found=True
        if rooms_data[chosen_key]["connections"][opposite_direction(direction_choice)] == False: #If generated room does not have a doorway in the correct direction.
            room_not_found=True
    
    return rooms_data[chosen_key]

def opposite_direction(direction):
    opposite = "south"
    if direction == "north":
        opposite = "south"
    elif direction == "east":
        opposite = "west"
    elif direction == "south":
        opposite = "north"
    else:
        opposite="east"
    return opposite

def room_options(current_room, visited_rooms):
    """ Used when in a room the player has already visited.
    Shows the directions to rooms the player has visited
    Tells the user about other directions they could go.
    """
    if current_room["connections"]["north"]==True:
        if visited_rooms[current_room["name"]]["connections"]["north"]!=True: #If the connection has been replaced with a room reference
            print(f"To the north is the {visited_rooms[current_room["name"]["connections"]["north"]]}")
        else:
            print("You can proceed north.")
    elif current_room["connections"]["east"]==True:
        if visited_rooms[current_room["name"]]["connections"]["east"]!=True: #If the connection has been replaced with a room reference
            print(f"To the north is the {visited_rooms[current_room["name"]["connections"]["east"]]}")
        else:
            print("You can proceed east.")
    elif current_room["connections"]["south"]==True:
        if visited_rooms[current_room["name"]]["connections"]["south"]!=True: #If the connection has been replaced with a room reference
            print(f"To the north is the {visited_rooms[current_room["name"]["connections"]["south"]]}")
        else:
            print("You can proceed south.")
    elif current_room["connections"]["west"]==True:
        if visited_rooms[current_room["name"]]["connections"]["west"]!=True: #If the connection has been replaced with a room reference
            print(f"To the north is the {visited_rooms[current_room["name"]["connections"]["west"]]}")
        else:
            print("You can proceed west.")



if __name__ == "__main__":
    rooms = {}
    room = create_room()

    # just re-names the room for the purpose of easier access later
    room_name = room["name"]
    rooms[room_name] = room

    print(room)

'''
#Testing add_desc()
data=read_json("database.json")
room=data["rooms"]["basement"]
add_desc(room)
'''