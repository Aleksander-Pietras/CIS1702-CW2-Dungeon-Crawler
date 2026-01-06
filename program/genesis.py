from program.extra_usefull.path_finder import file_path_finder_all
#from read_write_json.write_json import update_json

from program.rooms.rooms import create_room
from program.read_write_json.write_json import overwrite_json

if __name__ == "__main__":
    stop_creating=False
    while stop_creating==False:
        FILENAME = "database.json"
        FILE_PATH = file_path_finder_all(FILENAME)
        print(FILE_PATH)
        room = create_room()
        overwrite_json(room)
        if input("Type 'stop' to finish creation. \n") == "stop":
            stop_creating=True

