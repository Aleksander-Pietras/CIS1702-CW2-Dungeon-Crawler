''' This code is the main execution loop
The code in here should only be specifically relevent to the game
'''
import json

# This is bad and needs to be changes to importing all the modules seperatly because this way we also import all the variables
from read_write_json.read_json import *
from read_write_json.write_json import *

from rooms.rooms import *
from program.npc.npc_list import *


if __name__ == "__main__":
    while True:
        print(npcs) # this is a test
        
    # main execution loop