import json
from program.player_class.player import self.inventory

gold = [25]
swords = ["Copper Sword", "Bone Sword", "Sapphire Sword", "Mythic Sword"]
axes = ["Stone Axe", "Iron Axe"]
prices = [25, 30, 45, 60, 90, 160]


AxeChoice = int(input("Shopkeeper Angus: Well what can I do for ya?" + "Shopkeeper Angus: If you are looking for a weapon let me show you this. :\n[0] Stone Axe.... 30\n[1] Iron Axe.... 60\n"))

validAxe = False
while validAxe == False:
  if AxeChoice== 0:
        gold = gold-(prices[0])
        print("Shopkeeper Angus: Wise Choice good friend.\n".format(axes[0], gold))
        validAxe = True

  elif AxeChoice== 1:
        gold = gold-(prices[1])
        print("Shopkeeper Angus: Wise Choice good friend.\n".format(axes[1], gold))
        validAxe = True
    
else:
    AxeChoice = int(input("Shopkeeper Angus: This is not avaliable my friend, try again.\n"))


SwordChoice = int(input("Shopkeeper Angus: Well what can I do for ya?" + "Shopkeeper Angus: If you are looking for a weapon let me show you this. :\n[0] Copper Sword.... 25\n[1] Bone Sword.... 45\n[2] Sapphire Sword.... 90\n[3] Mythic Sword.... 160\n"))
validSword = False
while validSword == False:
  if SwordChoice== 0:
        gold = gold-(prices[0])
        print("Shopkeeper Angus: Wise Choice good friend.\n".format(swords[0], gold))
        validSword = True

  elif SwordChoice== 1:
        gold = gold-(prices[1])
        print("Shopkeeper Angus: Wise Choice good friend.\n".format(swords[1], gold))
        Sword = True

  elif SwordChoice== 2:
        gold = gold-(prices[2])
        print("Shopkeeper Angus: Wise Choice good friend.\n".format(swords[2], gold))
        validSword = True

  elif SwordChoice== 3:
        gold = gold-(prices[3])
        print("Shopkeeper Angus: Wise Choice good friend.\n".format(swords[3], gold))
        validSword = True 
else:
    AxeChoice = int(input("Shopkeeper Angus: This is not avaliable my friend, try again.\n"))   


print("Shopkeeper Angus: I'll be seeing you later friend.")
