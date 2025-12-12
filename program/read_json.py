''' This file program.read_json hold functions for reading from a JSON file
Ensures Defencive Coding
And prevents duplicates of this code being in all files
'''
import json
from path_finder import file_path_finder_all

def read_json(filename):
    try:
        with open(filename, mode="r") as f:
            data = json.load(f)
            
    except FileNotFoundError as error:
        print(f"Issue \n{error}")

    else:
        return data

def fetch_data(data_name, data):
    special_data = data[data_name]
    return special_data

''' LOCAL execution block
'''
if __name__ == "__main__":
    FILENAME = "database.json"
    file_path = file_path_finder_all(FILENAME)
    data = read_json(file_path)
    print(data)