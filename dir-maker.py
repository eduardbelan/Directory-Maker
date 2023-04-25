import os

# Notify user to check path & show current path
current_path = os.getcwd()
print(f"\nNOTE: Check file path first and adjust if necessary.\n"
      f"Current Path: {current_path}\n")

# Global Vars
FORBIDDEN_SYMBOLS = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', ' ']
FILE_TYPES = ["txt", "py", "html", "css", "js"]

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
    while os.path.exists(f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}"):
        dir_name = input(f"'{dir_name}' already exists.\nnew name dir {fruit_loops}: ")
        # Check for forbidden symbols
        while any(symbol in dir_name for symbol in FORBIDDEN_SYMBOLS):
            dir_name = input(f"don't use: {FORBIDDEN_SYMBOLS}\nnew name dir {fruit_loops}: ")
    # Make dir
    os.mkdir(f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}")

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
            while os.path.exists(f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}\\{file_name}.{file_type}"):
                file_name = input(f"'{file_name}' already exists.\nnew name file in {dir_name}: ")
                # Check for forbidden symbols
                while any(symbol in file_name for symbol in FORBIDDEN_SYMBOLS):
                    file_name = input(f"don't use: {FORBIDDEN_SYMBOLS}\nnew name file in {dir_name}: ")
            # Make file
            file_path = f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}\\{file_name}.{file_type}"
            open(file_path, "a").close()
            # Add file to file counter
            file_count += 1

# Ask user to overview created dir structure
#   - with current path
#   - dirs
#   - files
#for dirpath, dirnames, filenames in os.walk(f"C:\\Users\\eduar\\portfolio-projects"):
#
#    #remove unwanted directories so they don't show up
#    if ".git" and "venv" in dirnames:
#        dirnames.remove(".git")
#        dirnames.remove("venv")
#
#    print("Current Path:", dirpath)
#    print("Directories:", dirnames)
#    print("Files:", filenames)
#    print()


# Snippets
# make directory
# os.mkdir("C:\\Users\\eduar\\portfolio-projects\\test-dir")

# make file
# file_path = "C:\\Users\\eduar\\portfolio-projects\\test.txt"
# open(file_path, "a").close()

# make file and write to file
# with open(file_path, "w") as file:
#    insert text here
#    file.write("")


# Make this code work
#def show_directory_structure(path):
#    for dirpath, dirnames, filenames in os.walk(path):
#
#        #remove unwanted directories so they don't show up
#        if ".git" and "venv" in dirnames:
#            dirnames.remove(".git")
#            dirnames.remove("venv")
#
#        print("Current Path:", dirpath)
#        print("Directories:", dirnames)
#        print("Files:", filenames)
#        print()
#
#'# create three directories
#dir1 = "C:\\Users\\eduar\\portfolio-projects\\dir1"
#dir2 = "C:\\Users\\eduar\\portfolio-projects\\dir2"
#dir3 = "C:\\Users\\eduar\\portfolio-projects\\dir3"
#
#'# create a list of directory paths
#dirs = [dir1, dir2, dir3]
#
#'# call the function for each directory path in the list
#for dir in dirs:
#    show_directory_structure(dir)