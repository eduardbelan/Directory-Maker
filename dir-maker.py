import os
import sys

# Global Vars
ADJUST_PATH = "C:\\Users\\eduar\\portfolio-projects"
FORBIDDEN_SYMBOLS = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', ' ']
FILE_TYPES = ["txt", "py", "html", "css", "js"]
DIRS_CREATED = []
FILES_CREATED = []

# Notify user to check path & show current path
# Ask user if happy with current path
happy_path = input(f"\nNOTE: Check path first and adjust if necessary.\n\n"
                   f"Current Path: {ADJUST_PATH}\n\n"
                   f"Are you happy with this path? y/n: ")
# Check user input
if happy_path == "n":
    print("\n1. Please adjust path in global variable 'ADJUST_PATH'\n"
          "2. Restart Program")
    sys.exit()
else:
    pass
# Check user input until correct
while happy_path not in ["y", "n"]:
    happy_path = input(f"Are you happy with this path: {ADJUST_PATH}\n"
                       f"Type y/n: ")

    if happy_path == "n":
        print("\n1. Please adjust path in global variable 'ADJUST_PATH'\n"
              "2. Restart Program")
        sys.exit()
    else:
        pass

# Ask User how many dirs
is_int = False
while not is_int:
    try:
        num_dirs = int(input("num dirs: "))
        is_int = True
        if num_dirs >= 20:
            dir_much = input(f"do you want {num_dirs} dirs y/n: ")
            while dir_much not in ["y", "n"]:
                dir_much = input(f"for {num_dirs} dirs enter y/n: ")
            if dir_much == "n":
                is_int = False
            else:
                pass
    except ValueError:
        print("only num input valid")

# Loop to make dirs
fruit_loops = 0
for i in range(num_dirs):
    fruit_loops += 1
    # Ask User to name dirs
    dir_name = input(f"name dir {fruit_loops}: ")
    # Check for forbidden symbols
    while any(symbol in dir_name for symbol in FORBIDDEN_SYMBOLS):
        dir_name = input(f"don't use: {FORBIDDEN_SYMBOLS}\nnew name dir {fruit_loops}: ")
    # Check if dir name already exists
    while os.path.exists(f"{ADJUST_PATH}\\{dir_name}"):
        dir_name = input(f"'{dir_name}' already exists.\nnew name dir {fruit_loops}: ")
        # Check for forbidden symbols
        while any(symbol in dir_name for symbol in FORBIDDEN_SYMBOLS):
            dir_name = input(f"don't use: {FORBIDDEN_SYMBOLS}\nnew name dir {fruit_loops}: ")
    # Make dir
    os.mkdir(f"{ADJUST_PATH}\\{dir_name}")
    # Show a list of dirs created
    DIRS_CREATED.append(dir_name)
    print(f"Directories Created: {DIRS_CREATED}\n")
    # File counter
    file_count = 0
    # Ask user for multiple file creation
    while True:
        # Ask User if files
        file_dirs = input(f"files created in this dir: {dir_name} - {file_count}\n"
                          f"need file y/n: ").lower()
        # Check user input for y/n
        while file_dirs not in ["y", "n"]:
            file_dirs = input("invalid input, enter y/n for file: ")

        if file_dirs == "n":
            file_count = 0
            FILES_CREATED = []
            break

        else:
            # Ask User file type
            file_type = input("type file txt/py/html/css/js: ").lower()
            # Check user input for file type
            while file_type not in ["txt", "py", "html", "css", "js"]:
                file_type = input(f"invalid input, choose a file type from {FILE_TYPES}\nenter file type: ")
            # Ask User file name
            file_name = input("name file: ")
            # Check for forbidden symbols in file name
            while any(symbol in file_name for symbol in FORBIDDEN_SYMBOLS):
                file_name = input(f"don't use: {FORBIDDEN_SYMBOLS}\nnew name file in {dir_name}: ")
            # Check if file name already exists
            while os.path.exists(f"{ADJUST_PATH}\\{dir_name}\\{file_name}.{file_type}"):
                file_name = input(f"'{file_name}' already exists.\nnew name file in {dir_name}: ")
                # Check for forbidden symbols
                while any(symbol in file_name for symbol in FORBIDDEN_SYMBOLS):
                    file_name = input(f"don't use: {FORBIDDEN_SYMBOLS}\nnew name file in {dir_name}: ")

            # Make file
            file_path = f"{ADJUST_PATH}\\{dir_name}\\{file_name}.{file_type}"
            open(file_path, "a").close()
            # Show a list of files created
            FILES_CREATED.append(f"{file_name}.{file_type}")
            print(f"{FILES_CREATED}")
            # Add file to file counter
            file_count += 1

# Show user a structure of all dirs and files created in this format:
#   - Current Path:
#   - Directories:
#   - Files:

for i in DIRS_CREATED:
    ADJUST_PATH = f"{ADJUST_PATH}\\{i}"
    for dirpath, dirnames, filenames in os.walk(ADJUST_PATH):
        print(f"Current Path: ", dirpath)
        print(f"Directories: ", dirnames)
        print(f"Files: ", filenames)
        print()
    ADJUST_PATH = "C:\\Users\\eduar\\portfolio-projects"
