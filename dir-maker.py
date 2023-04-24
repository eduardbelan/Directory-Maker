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
    # Ask User if files
    file_dirs = input("need files y/n: ").lower()
    # Check user input for y/n
    while file_dirs not in ["y", "n"]:
        file_dirs = input("invalid input, enter y/n for file: ")

    if file_dirs == "n":
        pass
    else:
        # Ask User file type
        what_file = input("type file txt/py/html/css/js: ").lower()
        # Check user input for file type
        while what_file not in ["txt", "py", "html", "css", "js"]:
            what_file = input(f"invalid input, choose a file type from {file_types}\nenter file type: ")
        # Ask User file name
        file_name = input("name file: ")
        if what_file == "txt":
            # Make file txt
            file_path = f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}\\{file_name}.txt"
            open(file_path, "a").close()
        elif what_file == "py":
            # Make file py
            file_path = f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}\\{file_name}.py"
            open(file_path, "a").close()
        elif what_file == "html":
            # Make file html
            file_path = f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}\\{file_name}.html"
            open(file_path, "a").close()
        elif what_file == "css":
            # Make file css
            file_path = f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}\\{file_name}.css"
            open(file_path, "a").close()
        elif what_file == "js":
            # Make file js
            file_path = f"C:\\Users\\eduar\\portfolio-projects\\{dir_name}\\{file_name}.js"
            open(file_path, "a").close()

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
