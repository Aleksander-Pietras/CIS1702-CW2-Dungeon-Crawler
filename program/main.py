''' This code is the main execution loop
The code in here should only be specifically relevent to the game
'''
import json
import random
from program.extra_usefull.path_finder import file_path_finder_all
from program.read_write_json.read_json import read_json
from program.rooms.rooms import room_options
from program.rooms.rooms import choose_random_description
from program.rooms.rooms import decide_on_directions
from program.rooms.rooms import empty_room
from program.rooms.rooms import choose_next_room
from program.rooms.rooms import opposite_direction
from program.genesis import intro_text

from program.player_class.player import player


if __name__ == "__main__": #Please can you make the main execution loop modular? Even if you just put all this in a function, I'd be happier.-Sophia
    FILENAME = "database.json"
    FILE_PATH = file_path_finder_all(FILENAME)

    game_data = read_json(FILENAME)
    rooms_data = game_data["rooms"]
    enemies_data = game_data["enemies"]
    npcs_data = game_data["npcs"]

    start_room = rooms_data["Start Room"]
    current_room = start_room
    previous_room = start_room
    visited_rooms = {}
    direction_choice="north" #So direction choice is remembered between loops

    player1 = player()

    intro_text()
    try:
        while True: #End when player dies
            print("-"*14)
            
            print(f"You are in the {current_room["name"]}") # NOT TO BE THE FINAL TAKE
            
            choose_random_description(current_room)

            if not current_room["enemies_active"]:
                empty_room()

            if not current_room["visited"]:

                if current_room["enemies_active"]:
                    num = random.randint(1, 3)
                    enemies = []
                    if num == 1:
                        enemies.append(enemies_data["goblin"])
                    elif num == 2:
                        enemies.append(enemies_data["skeleton"])
                        enemies.append(enemies_data["goblin"])
                    else:
                        enemies.append(enemies_data["orc"])

                    player1.combat(enemies)

                    
                rooms_data[current_room["name"]]["visited"] = True
                visited_rooms[current_room["name"]] = current_room #Adds the room to visited dictionary.
                if current_room != start_room:
                    visited_rooms[current_room["name"]]["connections"][opposite_direction(direction_choice)] = previous_room["name"]
                    previous_room = current_room
                
                direction_choice = decide_on_directions(current_room)
                if visited_rooms[current_room["name"]]["connections"][direction_choice] != True: #If going the direction they just came from
                    new_room = rooms_data[visited_rooms[current_room["name"]]["connections"][direction_choice]]
                else:
                    new_room=choose_next_room(rooms_data, visited_rooms, direction_choice)

                #Makes a reference to the room connection in visited_rooms so we can see which exits go to which rooms.
                visited_rooms[current_room["name"]]["connections"][direction_choice] = new_room["name"]
            else:
                room_options(current_room, visited_rooms)
                
                if current_room != start_room:
                    visited_rooms[current_room["name"]]["connections"][opposite_direction(direction_choice)] = previous_room["name"]
                    previous_room = current_room
                
                direction_choice = decide_on_directions(current_room)
                going_to=visited_rooms[current_room["name"]]["connections"][direction_choice]
                if going_to!=True: #Visiting an already generated room
                    new_room=visited_rooms[going_to]
                else: #Visiting a new room
                    new_room=choose_next_room(rooms_data, visited_rooms, direction_choice)
                    visited_rooms[current_room["name"]]["connections"][direction_choice] = new_room["name"]
            
            
            current_room = new_room
                



    except KeyboardInterrupt:
        print("Exiting program")
        raise KeyboardInterrupt