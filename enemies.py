# Structure for entities of dungeon crawler
import json
import random
enemies = [
    {"enemy":"goblin", "attack":10, "health":50, "Gold_Drop": 5},
    {"enemy":"skeleton", "attack":15, "health":70, "Gold_Drop": 10},
    {"enemy":"orc", "attack":25, "health":90, "Gold_Drop": 15}
]
def enemy_encounter(enemies):
     enemy_p = random.choice(enemies)
     print(f"A wild {enemy_p['enemy']} appears! It has {enemy_p['attack']} attack and {enemy_p['health']} health.")
     if enemy_p['enemy'] == "goblin":
          print("The goblin growls and reaches for its dagger!")
     elif enemy_p['enemy'] == "skeleton":
            print("The skeleton directs its empty face towards you, preparing to strike!")
     else:   print("The orc roars fiercely, raising its huge axe!")
enemy_encounter(enemies)
