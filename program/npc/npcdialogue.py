# Dialogue for dungeon crawler NPCs

import json

def start():
    decision = input(" Input [1] To approach shopkeeper \n  Input [2] To return back to the dungeon \n ")
    if decision  == "1" :
        print(" \n Shopkeeper Angus: 'Well, what can I do for ya?")
    elif decision =="2" :
        print(" You have returned back to the dungeon. ")
        start2()
    else:
        print(" You have entered an incorrect input, try again!")
        start()  

def start2():
     decision = input(" Input [1] Player: 'I'am looking for a weapon' \n  Input [2] Player: 'Tell me about the informant Caelan \n")
     if decision == "1" :
         print(" \n Shopkeeper Angus: 'If you are looking for a weapon let me show you this.'")
     elif decision =="2":
         print(" \n Shopkeeper Angus: 'Sometimes I think that Caelan talks too much, I suppose thats his calling in life. If I could bend steel as much as he could bend your ear then I could make a suit of crystal plates fit enough for an emperor!' ")
         start3()
     else:
        print(" You have entered an incorrect input, try again!")
        start2()

def start3():
    decision = input(" Input [1] Exit the shop \n Input [2] Ask the shopkeeper something else \n ")
    if decision == "1" :
        print(" \n Shopkeeper Angus: ' I'll be seeing you later friend.")
    elif decision =="2" :
        start2()  
    else: 
        print(" You have entered an incorrect input, try again!")
        start3()  


def start4():
    decision = input(" Input [1] Approach Caelan the Informant \n  Input [2] To return back to the dungeon \n ")
    if decision == "1":
        print(" \n Caelan the Informant: 'Hello my frined, stay for a while and listen.' ")
    elif decision =="2" :
        print(" You have returned back to the dungeon. ")
        start5()
    else: 
        print(" You have entered an incorrect input, try again!")
        start4() 

def start5():
    decision = input(" Input [1] Ask Caelan about Angus the Shopkeeper \n Input [2] Ask Caelan about the dungeon \n ")  
    if decision =="1":
        print(" \n Caelan the Informant:' Angus is a man of great action, I imagined he never told you about this but he once did venture into the tombs himself years ago. He knows his fair share of danger. He is now a skilled craftsman and he is willing to help anyone with his courage and honesty.' ")
    elif decision =="2":
        print(" \n Caelan the Informant: 'While venturing deeper into the tombs you may find information that even I could not tell you my friend.")
        start6()
    else: 
        print(" You have entered an incorrect input, try again!")
        start5()   

def start6():
    decision = input(" Input [1] Ask Caelan about the 'Dark Lord' \n Input [2] Ask Cealan about 'The Butcher' \n  ")
    if decision =="1":
        print(" \n The evil that you is ahead is the dark Lord of hell. Long before that evil was once imprisoned inside these tombs and the dark Lord once voweled that it rise from it's shackles a thousand years ago so it is your task to find the monster and elimate it for good. ")
    elif decision =="2":
        print(" \n Caelan the Informant: 'I've heard many myths and legends of a hidden away chamber within these tombs and there lies a foul beast who impales his victims on top of spears to keep as trophies. Many brave warriors have tried to challenge the dark evil only to never be seen again. Tread carefully my friend.")
        start7()
    else: 
        print(" You have entered an incorrect input, try again!")
        start6()    

def start7():
    decision = input(" Input [1] Ask Caelan something else \n Input [2] Return to the Dungeon")
    if decision =="1":
        start5()
    elif decision =="2":
        print("You have returned back to the dungeon.") 
    else: 
        print(" You have entered an incorrect input, try again!")
        start7()    

def start8():
    decision = input("Input [1] Head straight to the dungeon \n Input[2] Interact with Cain the Dungeon Keeper \n")
    if decision =="1":
        print("You have returned back to the dungeon.")
    elif decision =="2":
        print(" \n Cain the Dungeon Keeper: 'I have seen many like you enter these haunted tombs and never return.' ") 
    else: 
        print(" You have entered an incorrect input, try again!")
        start8()     

def start9():
    decision = input(" Input [1] Charge towards 'The Butcher' \n  Input [2] Run away from 'The Butcher' \n ")    
    print(" Your choice doesn't matter.  The Butcher: 'Ahh. Freash meat!") 

def start10():
    decision = input("Input [1] Charge towards 'The Dark Lord' \n  Input [2] Run away from 'The Dark Lord' \n ")
    print(" Your choice doesn't matter. Dark Lord: 'You dare disturb me mortal!" )