# Directory-Maker

## Description
Directory-Maker is a command-line program that allows users to easily create directories and files with custom names and file types. It provides a simple and convenient way to organize your files and folders based on your specific needs.

## Installation
To use Directory-Maker, follow these steps:

1. Clone the GitHub repository to your local machine.
2. Ensure you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the cloned directory.
4. Run the program using the following command:

```bash
python dir-maker.py
```

## Usage
When you run the Directory-Maker program, it will prompt you to provide the following information:

1. **Path**: Enter the desired path where you want to create the directories. The path has to be adjusted in the `dir-maker.py` file.
```python
# Global Vars
ADJUST_PATH = "C:\\<path-of-choice>"
# Example Path
ADJUST_PATH = "C:\\Users\\Username\\Desktop"
```
2. **Number of Directories**: Specify the total number of directories you want to create.
3. **Directory Names**: Provide names for each directory.
4. **Include Files**: Choose whether you want to include files in the directories or not. The program lets you name the files.
5. **File Types**: Select the file types you want to include in the directories `(e.g., txt, py, html, css, js)`.
```python
# Global Vars
# Add any file types you like
FILE_TYPES = ["txt", "py", "html", "css", "js"]
```

Once you provide the necessary inputs, the program will create the directories and, if selected, populate them with the specified files.

## Overview
After the program finishes executing, it will display an overview of the directories and files created. This summary will help you quickly review and verify the directory structure and file contents.

Feel free to explore and modify the Directory-Maker program according to your specific requirements.

## License
Directory-Maker is released under the [MIT License](https://opensource.org/licenses/MIT).

**Note:** This program is provided as-is without any warranty. Use it at your own risk.

## Contributions
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request or open an issue on the GitHub repository.

Happy directory creation with Directory-Maker!