import subprocess


def remove_virtual_environment():
    """
    Attempts to remove the virtual environment folder in the root directory.
    """
    subprocess.run(["rm", "-rf", ".venv"], check=True)
    print("Virtual environment removed")


def main():
    remove_virtual_environment()


if __name__ == "__main__":
    main()