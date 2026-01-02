''' This code is the main execution loop
The code in here should only be specifically relevent to the game
'''
import json
import random
from program.extra_usefull.path_finder import file_path_finder_all
from program.read_write_json.read_json import read_json
from program.rooms.rooms import choose_room
from program.rooms.rooms import choose_random_description
from program.rooms.rooms import decide_on_directions

def empty_room():
    """Displays text to say the same thing in different ways."""
    rand_text=random.randint(0,3)
    if rand_text==0:
        print("The room is empty")
    elif rand_text==1:
        print("There's nothing in this room.")
    elif rand_text==2:
        print("This room is eerily quiet. There's nothing here.")

def room_options(current_room, visited_rooms):
    """Used when in a room the player has already visited.
    Shows the directions to rooms the player has visited
    Tells the user about other directions they could go."""
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
    

if __name__ == "__main__": #Please can you make the main execution loop modular? Even if you just put all this in a function, I'd be happier.-Sophia
    FILENAME = "database.json"
    FILE_PATH = file_path_finder_all(FILENAME)

    game_data = read_json(FILENAME)
    rooms_data = game_data["rooms"]
    # enemies_data = game_data["enemies"] # Still waiting for Logan to add enemies
    npcs_data = game_data["npcs"]

    start_room = rooms_data["test_room"] # This is temporary until real rooms exist
    current_room = start_room
    visited_rooms = {}
    try:
        while True:
            # >>>>>>>> Some intro text here
            print(f"You are in the {current_room["name"]}") # NOT TO BE THE FINAL TAKE
            

            description = choose_random_description(current_room)      
            print(description)

            if not current_room["enemies_active"]:
                empty_room() #Outputs one of 3 options saying the room is empty.

            
            
            if not current_room["visited"]:
                direction_choice = decide_on_directions(current_room)
                rooms_data[current_room["name"]]["visited"] = True
                visited_rooms[current_room["name"]] = current_room #Adds the room to visited list.
                #Note: Make sure new_room is chosen from the rooms_data that exists in this place as it will be changed during execution in meaningful ways where the data in the file will not.
                #new_room=choose_next_room(rooms_data)

                #Makes a reference to the room connection in visited_rooms so we can see which exits go to which rooms.
                #visited_rooms[current_room["name"]]["connections"][direction_choice] = new_room["name"]
            else:
                room_options()
                direction_choice = decide_on_directions(current_room)
                going_to=visited_rooms[current_room["name"]]["connections"][direction_choice]
                if going_to!=True: #Visiting an already generated room
                    new_room=visited_rooms[going_to]
                else: #Visiting a new room
                    #new_room=choose_next_room(rooms_data)
                    #visited_rooms[current_room["name"]]["connections"][direction_choice] = new_room["name"]
                    pass
                



    except KeyboardInterrupt:
        print("Exiting program")
        raise KeyboardInterrupt