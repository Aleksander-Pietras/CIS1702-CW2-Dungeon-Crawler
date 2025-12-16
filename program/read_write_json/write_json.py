''' This program will be used to write/add new data to the JSON file
This is so that, we do not write data into the JSON manualy
'''
import json
from program.extra_usefull.path_finder import file_path_finder_all
from program.read_write_json.read_json import read_json

def overwrite_json(path, filename, new_data):
    current_data = read_json(FILENAME)

    print("-" * 30)
    print(f"Overwriting file: {filename}")
    print(f"This action will delete all data currently in {filename}:\ndata in {filename}")
    print(current_data)
    confirm = input("Type YES to overwrite:\n")
    if confirm.strip().upper() == "YES":
        with open(path, mode="w") as f:
            json.dump(new_data, f, indent=4)
            print("File overwriten sucessfully")

''' Main Execution cycle
Just in case we ever decide to use these functions
'''
if __name__ == "__main__":
    FILENAME = "database.json"
    FILE_PATH = file_path_finder_all(FILENAME)

# this only exists temporarily as my test data, feel free to delete when you are ready to add actual data
    data = {
        "rooms": {
            1: "stats", 2: "stats"
        },
        "entities": {
            "NPC": {
                "npc1": [
                    "diaulouge", {"shop items": "shop prices"}
                ]
            },
            "enemies": {
                "more random space wasiting info": "this is only here so that the database is not empty"
            }
        }
    }

    overwrite_json(FILE_PATH, FILENAME, data)
    