from program.extra_usefull.path_finder import file_path_finder_all
#from read_write_json.write_json import update_json

from program.rooms.rooms import create_room


if __name__ == "__main__":
    while True:
        FILENAME = "database.json"
        FILE_PATH = file_path_finder_all(FILENAME)
        print(FILE_PATH)
        room = create_room()

