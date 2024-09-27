# Python venv automation

This is a program to automate the creation of virtual environment and installation of required packages.

## Project Status ![Status](https://img.shields.io/badge/status-completed-brightgreen)

1. The core functionality is completed and includes:
    - Installing and creating virtual environment
    - Removing virtual environment
    - Appending gitignore file

## System Requirements:
    python3
    pip
    Linux operating system


## Usage:
1. Install and create virtual environment
    python3 install_venv.py

2. Activate virtual environment
    source .venv/bin/activate

3. Install required packages, and run your program of choice! e.g:
    pip install -r requirements.txt
    python3 main.py

4. Deactivate virtual environment
    deactivate

5. Remove virtual environment
    python3 remove_venv.py

