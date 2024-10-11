import logging
import shutil
from pathlib import Path

_logger = logging.getLogger(__name__)


def clear_directory(directory: Path = Path("temp")) -> None:
    """
    Clear all files and subdirectories from the specified directory.

    Usage:

    ```python
    clear_directory(Path("your_directory"))
    ```
    """
    for item in directory.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def delete_directory(directory: Path = Path("temp")) -> None:
    """
    Delete the specified directory and its contents.

    Usage:

    ```python
    delete_directory(Path("your_directory"))
    ```
    """
    if directory.exists() and directory.is_dir():
        _logger.info("Deleting %s...", directory)
        shutil.rmtree(directory)
        _logger.info("%s has been deleted.", directory)
    else:
        _logger.warning("%s does not exist or is not a directory.", directory)


def create_directory(directory: Path = Path("temp")) -> None:
    """
    Create the specified directory and its contents.

    Note: this will clear all files in the directory if it already exists.

    Usage:

    ```python
    _create_directory(Path("your_directory"))
    ```
    """
    if directory.exists() and directory.is_dir():
        _logger.info("%s already exists.", directory)
        clear_directory(directory)
    else:
        _logger.info("Creating %s...", directory)
        directory.mkdir(parents=True)
        _logger.info("%s has been created.", directory)
