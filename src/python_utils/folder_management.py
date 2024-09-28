from pathlib import Path
import shutil

def clear_directory(directory: Path = Path("temp")):
    """
    Clears all files and subdirectories from the specified directory.

    Usage:

    ```python
    _clear_directory(Path("your_directory"))
    ```
    """
    for item in directory.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def delete_directory(directory: Path = Path("temp")):
    """
    Deletes the specified directory and its contents.

    Usage:

    ```python
    _delete_directory(Path("your_directory"))
    ```
    """
    if directory.exists() and directory.is_dir():
        print(f"Deleting {directory}...")
        shutil.rmtree(directory)
        print(f"{directory} has been deleted.")
    else:
        print(f"{directory} does not exist or is not a directory.")


def create_directory(directory: Path = Path("temp")):
    """
    Create the specified directory and its contents.

    Usage:

    ```python
    _create_directory(Path("your_directory"))
    ```
    """
    if directory.exists() and directory.is_dir():
        print(f"{directory} already exists.")
        clear_directory(directory)
    else:
        print(f"Creating {directory}...")
        directory.mkdir(parents=True)
        print(f"{directory} has been created.")
