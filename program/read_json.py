''' This file program.read_json hold functions for reading from a JSON file
Ensures Defencive Coding
And prevents duplicates of this code being in all files
'''
import json

def read_json(FILENAME: str):
    try:
        with open(FILENAME, mode="r") as f:
            reader = f.read()

    except FileNotFoundError as Error:
        print(Error)
        
    else:
        return reader