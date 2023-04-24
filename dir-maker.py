import os

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
forbidden_symbols = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', ' ']
file_types = ["txt", "py", "html", "css", "js"]
fruit_loops = 0
for i in range(num_dirs):
    fruit_loops += 1
    # Ask User to name dirs
    dir_name = input(f"name dir {fruit_loops}: ")
    # Check for forbidden symbols
    while any(symbol in dir_name for symbol in forbidden_symbols):
        dir_name = input(f"don't use: {forbidden_symbols}\nnew name dir {fruit_loops}: ")
    # Check if dir name already exists
    while os.path.exists(f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}"):
        dir_name = input(f"'{dir_name}' already exists.\nnew name dir {fruit_loops}: ")
        # Check for forbidden symbols
        while any(symbol in dir_name for symbol in forbidden_symbols):
            dir_name = input(f"don't use: {forbidden_symbols}\nnew name dir {fruit_loops}: ")
    # Make dir
    os.mkdir(f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}")

    # File counter
    file_count = 0
    # Ask user for multiple file creation
    while True:
        # Ask User if files
        file_dirs = input(f"files created in this dir {file_count}\n"
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
                file_type = input(f"invalid input, choose a file type from {file_types}\nenter file type: ")
            # Ask User file name
            file_name = input("name file: ")
            # Check for forbidden symbols in file name
            while any(symbol in file_name for symbol in forbidden_symbols):
                file_name = input(f"don't use: {forbidden_symbols}\nnew name file in {dir_name}: ")
            # Check if file name already exists
            while os.path.exists(f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}\\{file_name}.{file_type}"):
                file_name = input(f"'{file_name}' already exists.\nnew name file in {dir_name}: ")
                # Check for forbidden symbols
                while any(symbol in file_name for symbol in forbidden_symbols):
                    file_name = input(f"don't use: {forbidden_symbols}\nnew name file in {dir_name}: ")
            # Make file
            file_path = f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}\\{file_name}.{file_type}"
            open(file_path, "a").close()
            # Add file to file counter
            file_count += 1


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
