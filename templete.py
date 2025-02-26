import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "textsummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",  # Fixed typo: "conponents" -> "components"
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",  # Fixed filename issue
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",  # Fixed filename issue
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",  # Fixed typo: "requiremetns.txt" -> "requirements.txt"
    "setup.py",
    "research/trials.ipynb"  # Fixed typo: "trails.ipynb" -> "trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Corrected `path` to `Path`
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)  # Fixed `exits_ok` to `exist_ok`
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()  # Creates an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")