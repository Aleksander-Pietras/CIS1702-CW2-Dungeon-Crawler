import json
import random
from program.read_write_json.read_json import *

class player:
    def __init__(self):
        self.health = 100
        self.lives = 3
        self.enemies_defeated = 0
        self.inventory = []
        ''' WE could have a dir or a matrix if we wish to have max inventory space determined by weight
        - Where each item has a weight and the player can hold a max weight
        
        OR we could just count items and make sure player cannot hold more then a max # of items
        '''

    def combat(self, enemies):
        ''' Combat takes place in turns
        cycling through the list as enemies are defeated
        '''

        for enemy in enemies:
            while enemy["health"] > 0:
                print(f"{enemy["enemy"]} is attacking you")
                # defence phase
                print(f"You recived {enemy["attack"]} damage")

                self.health -= enemy["attack"]
                if self.health <= 0:
                    print("All health is lost")
                    self.lives -= 1
                    print("One life is lost")

                    if self.lives == 0:
                        print("All lives are lost")
                        print("GAME OVER")
                        print(f"You have defeated {self.enemies_defeated} enemies")
                        exit()

                    print(f"You have {self.lives} remaining")

                # attack phase
                sucess = random.random(0, 1)
                damage = 10 * sucess + (self.enemies_defeated * 0.3)

                enemy["health"] -= damage

        print("All enemies are defeated")
        print(f"You have recovered 20 health")
        self.health += 20
                

