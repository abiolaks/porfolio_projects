# logic for project structure creation

# imports the necessary modules for file and directory operations
import os
from pathlib import (
    Path,
)  # for handling filesystem paths. it convert to path object for the operating system

# import shutil  # for high-level file operations like copying and removing directories
import logging  # for logging messages

# sets up logging configuration
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")
# This line sets up logging so that all INFO and higher messages are printed, each prefixed with a timestamp and formatted as shown.

# define your project name
PROJECT_NAME = "wine_quality_prediction"

# list of folder and the respective files to be created in the project structure
list_of_files = [
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/constant/__init__.py",
    f"src/{PROJECT_NAME}/logging/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]


# loop through the list of files and create them if they don't exist
for filepath in list_of_files:
    filepath = Path(
        filepath
    )  # convert the list object to a path object for the operating system

    # split the directory and file name from the path object
    filedir, filename = os.path.split(filepath)

    # FIX: Always create the directory if filedir is not empty (for files in subfolders)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # FIX: File creation logic must be outside the 'if filedir != ""' block
    # This ensures files in the root directory (filedir == "") are also created
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
