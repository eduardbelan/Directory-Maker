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
