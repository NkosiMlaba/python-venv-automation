# Python venv automation

This is a program to automate the installation and creation of virtual environment.

## Summary:
The development of this came out of the need to automate the installation and creation of virtual environment. For people who run multiple projects and do not want to install each project's dependencies system wide. They can use python's virtual environment to install the dependencies for each project. 

This program will automate the installation and creation of virtual environment. Additionally it will append the gitignore file with the virtual environment directory if needed. It will also remove the virtual environment if needed.

Simply place the scripts in the root directory of your project and follow the usage instructions below. 

## Project Status ![Status](https://img.shields.io/badge/status-completed-brightgreen)

1. The core functionality is completed and includes:
    - Installing and creating virtual environment
    - Removing virtual environment
    - Appending gitignore file

## System Requirements:
- python3
- pip
- Linux operating system


## Usage:
1. Install and create virtual environment
        
        python3 install_venv.py

2. Activate virtual environment
        
        source .venv/bin/activate

3. Install required packages, and run your program of choice! (for demonstration purposes only, will not work):
        
        pip install -r requirements.txt
        python3 main.py

4. Deactivate virtual environment
        
        deactivate

5. Remove virtual environment
        
        python3 remove_venv.py



