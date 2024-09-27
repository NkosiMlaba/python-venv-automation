import os


def append_to_gitignore(gitignore_path, entry):
    """
    Append the specified entry to the .gitignore file if it's not already present.
    """
    with open(gitignore_path, 'a') as gitignore_file:
        gitignore_file.write(f"{entry}\n")
        print(f"'{entry}' has been added to {gitignore_path}.")


def is_venv_present_in_gitignore(gitignore_path, entry):
    """
    Check if the specified entry is already present in the .gitignore file.
    """
    with open(gitignore_path, 'r') as gitignore_file:
        content = gitignore_file.read()

    if entry in content:
        print(f"'{entry}' is already in {gitignore_path}. Exiting.")
        return True
    else:
        return False


def create_gitignore_with_venv(gitignore_path, entry):
    """
    Create a .gitignore file with .venv in the file content.
    """
    with open(gitignore_path, 'w') as gitignore_file:
        gitignore_file.write(f"{entry}\n")
        print(f"{gitignore_path} created with '{entry}'.")


def main():
    gitignore_path = ".gitignore"
    entry = ".venv"

    if os.path.exists(gitignore_path):
        if not is_venv_present_in_gitignore(gitignore_path, entry):
            append_to_gitignore(gitignore_path, entry)
    else:
        create_gitignore_with_venv(gitignore_path, entry)


if __name__ == "__main__":
    main()
