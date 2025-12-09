''' This program will be used to write/add new data to the JSON file
This is so that, we do not write data into the JSON manualy
'''

import json

"""Writes everything to file in the form of a list of lists of dictionaries."""
def write_rooms(room_list, loot_list, monster_list): #For now has the lists taken as an argument. Idk if that's what I'm supposed to do.
    list_of_lists = [room_list, loot_list, monster_list]
    jtext = json.dumps(list_of_lists, indent=4)
    with open("dungeon_crawler_content.json", "w") as f:
        f.write(jtext)

"""Loads the information from the json and returns the list that contains the lists of dictionaries."""
def load_content():
    list_of_lists = []
    try:
        with open("dungeon_crawler_content.json", "r") as f:
            json_content = f.read()
            list_of_lists = json.loads(json_content)
    except:
        print("ERROR:File not found.")
        #We'll probably need more than just an error message if the data has failed to load.
    return list_of_lists

"""Used for running other methods. Dictates the order things are done."""
def main():
    #Loads lists and seperates them
    list_of_lists = load_content()
    room_list = list_of_lists[0]
    loot_list = list_of_lists[1]
    monster_list = list_of_lists[2]
    
    write_rooms(room_list, loot_list, monster_list) #Useful for when we want to change stuff, even if it won't actually be used in game running.


''' Main Execution cycle
Just in case we ever decide to use these functions
'''
if __name__ == "__main__":
    main()