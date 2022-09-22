import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s:%(levelname)s]:%(message)s"
    )

while True:
    project_name = input("enter the project name : ")
    if project_name != '':
        break

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    "test/__init__.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "setup_init.sh",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "requirements.txt",
    "requirements_dev.txt",
    "tox.ini",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory at : {filedir} for file : {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize()==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating a new file : {filename} at path : {filepath}")
    else:
        logging.info(f"file is already present at : (filepath)")

