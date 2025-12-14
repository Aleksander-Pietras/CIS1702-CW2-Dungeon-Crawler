''' This program will be used to write/add new data to the JSON file
This is so that, we do not write data into the JSON manualy
'''
import json
from program.extra_usefull.path_finder import file_path_finder_all

def overwrite_json(path, filename, new_data):
    ''' Safely overwrite JSON file ONLY when called intentionally
    - Requires user autharisation
    - Only runs in file: write_json.py
    '''
    if __name__ != "__main__":
        raise PermissionError(
            "function: overwrite_json can only run in write_json.py"
            )
    try:
        with open(path, mode="r") as f:
            current_data = json.load(f)

    except:
        print("The function: overwrite_json has ran into an unknown issue")
        raise Exception("Crashed on purpose to FORCE stop the function")
    
    else:
        print("-" * 30)
        print(f"Overwriting file: {filename}")
        print(f"This action will delete all data currently in {filename}:\ndata in {filename}")
        print(current_data)
        confirm = input("Type YES to overwrite:\n")
        if confirm.strip().upper() != "YES":
            raise Exception("Chrashed on purpose")
        
        with open(path, mode="w") as f:
            json.dump(new_data, f, indent=4)
            print("File overwriten sucessfully")

def add_json(path, data):
    try:
        with open(path, mode="a") as f:
            json.dump(data, f, indent=4)
    
    except FileNotFoundError as error:
        print(f"Issue \n{error}")


''' Main Execution cycle
Just in case we ever decide to use these functions
'''
if __name__ == "__main__":
    FILENAME = "database.json"
    FILE_PATH = file_path_finder_all(FILENAME)

# this only exists temparely as my test data, feel free to delete when you are ready to add actual data
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

    add_json(FILE_PATH, data)
    overwrite_json(FILE_PATH, FILENAME, data)
    