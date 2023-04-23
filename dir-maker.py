import os

# Ask User how many dirs
num_dirs = int(input("num dirs: "))

# Loop to make dirs
fruit_loops = 0
for i in range(num_dirs):
    fruit_loops += 1
    # Ask User to name dirs
    name_dirs = input(f"name dir {fruit_loops}: ")
    # Make dir
    os.mkdir(f"C:\\Users\\eduar\\portfolio-projects\\{name_dirs}")
    # Ask User if files
    file_dirs = input("need files y/n: ").lower()
    if file_dirs == "n":
        pass
    else:
        # Ask User file type
        what_file = input("type file txt/py: ").lower()
        # Ask User file name
        file_name = input("name file: ")
        if what_file == "txt":
            # Make file
            file_path = f"C:\\Users\\eduar\\portfolio-projects\\{name_dirs}\\{file_name}.txt"
            open(file_path, "a").close()
        else:
            # Make file
            file_path = f"C:\\Users\\eduar\\portfolio-projects\\{name_dirs}\\{file_name}.py"
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
