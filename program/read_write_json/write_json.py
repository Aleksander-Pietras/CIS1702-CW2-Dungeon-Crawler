''' This program will be used to write/add new data to the JSON file
This is so that, we do not write data into the JSON manualy
'''
import json
from program.extra_usefull.path_finder import file_path_finder_all
from program.read_write_json.read_json import read_json

def overwrite_json(new_data):
    'Updates the database.json with new data.'
    'Can only add one dictionary at a time'
    filename=FILENAME
    path=FILE_PATH
    current_data = read_json(filename)

    print("-" * 30)
    print(f"Overwriting file: {filename}")
    print(f"This action will update the data currently in {filename}:\ndata in {filename}")
    print(current_data)

    if "visited" in new_data: #Checks if the data has a key that is unique to rooms to check if the data is a room.
        rooms=current_data["rooms"]
        rooms[new_data["name"]] = new_data
        current_data["rooms"] = rooms
    elif "enemy" in new_data: #Checks if the data has a key that is unique to monsters to check if the data is a monster
        monsters=current_data["monsters"]
        monsters[new_data["enemy"]] = new_data
        current_data["monsters"] = monsters
    #elif loot
    else: #NPCs have inconsistent keys so I'm putting them in the else.
        npcs=current_data["npcs"]
        npcs[new_data["name"]] = new_data
        current_data["npcs"] = npcs

    
    confirm = input("Type YES to overwrite:\n")
    if confirm.strip().upper() == "YES":
        with open(path, mode="w") as f:
            json.dump(current_data, f, indent=4)
            print("File overwriten sucessfully")

''' Main Execution cycle
Just in case we ever decide to use these functions
'''
if __name__ == "__main__":
    FILENAME = "database.json"
    FILE_PATH = file_path_finder_all(FILENAME)

# this only exists temporarily as my test data, feel free to delete when you are ready to add actual data
    data = {"name": "basement","description":"You fall down a shaft into a basement","visited":False,"npc_active":False,"enemies_active":False,"extra_function_active":False,"active":False}
    overwrite_json(data)
    