npcs = {
    "Shopkeeper Angus": {
        "intro text": "Well what can I do for ya?",
        "Open Shop": "If you are looking for a weapon let me show you this.",
        "Gossip" : "'Sometimes I think that Caelan talks too much, I suppose thats his calling in life. If I could bend steel as much as he could bend your ear then I could make a suit of crystal plates fit enough for an emperor!'",
        "GoodBye": "I'll be seeing you later friend.",
       # here we can put other stuff here like shop items
    },
    

    "Informat Caelan": {
        "name": "Caelan the Informat",
        "into text": "Hello my frined, stay for a while and listen",
        "Gossip":"Angus is a man of great action, I imagined he never told you about this but he once did venture into the tombs himself years ago. He knows his fair share of danger. He is now a skilled craftsman and he is willing to help anyone with his courage and honesty.",
        "Gossip2": "While venturing deeper into the tombs you may find information that even I could not tell you my friend.",
        "Dark Lord Gossip": "The evil that you is ahead is the dark Lord of hell. Long before that evil was once imprisoned inside these tombs and the dark Lord once voweled that it rise from it's shackles a thousand years ago so it is your task to find the monster and elimate it for good.",
        "The Butcher Gossip": "I've heard many myths and legends of a hidden away chamber within these tombs and there lies a foul beast who impales his victims on top of spears to keep as trophies. Many brave warriors have tried to challenge the dark evil only to never be seen again. Tread carefully my friend.",
        "Goodbye": "Stay safe out there good friend",

    },

    "Dungeon Keeper Cain": {
        "name": "Cain the Dungeon Keeper",
        "intro text": "I have seen many like you enter these haunted tombs and never return."
    },

    "The Butcher": {
        "name": "The Butcher",
        "intro text": "Ahh. Freash meat!"
    },
    "The Dark Lord": {
        "name": "The Dark Lord",
        "intro text": "You dare disturb me mortal!"
    },
    
}

if __name__ == "__main__":
    print( list(npcs.keys()) )