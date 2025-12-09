''' This file program.read_json hold functions for reading from a JSON file
Ensures Defencive Coding
And prevents duplicates of this code being in all files
'''
import json

def read_json(filename):
    try:
        with open(filename, mode="r") as f:
            data = json.load(f)
            
    except FileNotFoundError as error:
        print(f"Issue \n{error}")

    else:
        return data


''' MAIN execution block
'''
if __name__ == "__main__":
    FILENAME = "database.json"
    read_json(FILENAME)