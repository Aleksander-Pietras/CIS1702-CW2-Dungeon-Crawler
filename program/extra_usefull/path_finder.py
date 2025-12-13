''' This code finds the path of the files
- created after i ran into an issue with opening "database.json"

can be used to find any file on the branch
'''
import os

def file_path_finder_all(filename: str, relative_root: str = "."):
    files = os.scandir(relative_root)
    for entry in files:
        if entry.name == filename:
            return entry.path

        if entry.is_dir() and entry.name != ".git":
            file_path = file_path_finder_all(filename, entry.path)
            if file_path != None:
                return file_path

''' LOCAL execution loop
'''
if __name__ == "__main__":
    filename = input("Enter the name of the file you are looking for: ")
    file_path = file_path_finder_all(filename, '.')

    if file_path != None:
        print(f"Found the file: {filename}")
        print(f"Path: {file_path}")

    else:
        print(f"File: {filename} does not exist")