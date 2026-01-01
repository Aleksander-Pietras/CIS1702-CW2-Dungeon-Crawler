''' This code is the main execution loop
The code in here should only be specifically relevent to the game
'''
import json
from program.extra_usefull.path_finder import file_path_finder_all
from program.read_write_json.read_json import read_json
from program.rooms.rooms import choose_room
from program.rooms.rooms import choose_random_description
from program.rooms.rooms import decide_on_directions

if __name__ == "__main__":
    FILENAME = "database.json"
    FILE_PATH = file_path_finder_all(FILENAME)

    game_data = read_json(FILENAME)
    rooms_data = game_data["rooms"]
    # enemies_data = game_data["enemies"] # Still waiting for Logan to add enemies
    npcs_data = game_data["npcs"]

    start_room = rooms_data["test_room"] # This is temporary until real rooms exist
    current_room = start_room
    try:
        while True:
            # >>>>>>>> Some intro text here
            print(f"You are in the {current_room["name"]}") # NOT TO BE THE FINAL TAKE
            if not current_room["visited"]:
                current_room["visited"] = True 

            description = choose_random_description(current_room)      
            print(description)

            if not current_room["enemies_active"]:
                print("The rooms is empty") # could do with a function that has different ways to say this message

            direction_choice = decide_on_directions(current_room)


    except KeyboardInterrupt:
        print("Exiting program")
        raise KeyboardInterrupt






