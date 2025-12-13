import json
from program.read_write_json.read_json import *

class player:
    def __init__(self):
        self.position = 0 # whatever the system is for room tracking
        self.health = 100
        self.inventory = []
        ''' WE could have a dir or a matrix if we wish to have max inventory space determined by weight
        - Where each item has a weight and the player can hold a max weight
        
        OR we could just count items and make sure player cannot hold more then a max # of items
        '''

    def move(self, direction):
        ''' direction: input from user
        - used for selecting rooms
        '''
        raise NotImplementedError
    # not implemented error to ensure its obvious that the function does not work

    def combat(self, enemies: list):
        ''' Combat takes place in turns
        cycling through the list as enemies are defeated
        '''
        raise NotImplementedError

        for enemy in enemies:
            while enemy[1] >= 0:
                pass
            # some sort of fight mechanic