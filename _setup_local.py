from os.path import exists, join
from os import listdir
from shutil import copytree
from pathlib import Path
from typing import Tuple


def verify_virtual_env(path: str) -> bool:
    """Verify if exists virtual env

    Args:
        path (str): Absolute path to project

    Raises:
        FileNotFoundError: Case the virtual env not found

    Returns:
        bool: True if virtual env exists
    """
    if exists(path):
        return True
    raise FileNotFoundError("VIRTUAL ENV NOT FOUND!")


def copy_external_modules(absolute_path: str, directories: Tuple[Tuple[str]]) -> None:
    """Copy external modules

    Args:
        absolute_path (str): Absolute path to project
        directories (Tuple[Tuple[str]]): Tuple of tuples, the first tuple is a
        module to copy, the second tuple is a absolute path to destination the module.
    """

    path_to_directory_packages = join(
        absolute_path, "lib", listdir(f"{absolute_path}lib")[0], "site-packages", ""
    )

    print(f"Python packages : {path_to_directory_packages}")

    for directory in directories:

        external_modules_path = join(absolute_path, directory[1])
        print(f"Path to external: {external_modules_path}")

        path = join(path_to_directory_packages, directory[0], "")

        try:
            copytree(path, join(external_modules_path, directory[0]), False, None)
            print(f"Package {directory[0]} copied with success")
        except FileNotFoundError:
            print(f"Package not found : {directory[0]}")
        except FileExistsError:
            print(f"Exists : {directory[0]}")
        except Exception as err:
            print(f"ERR : {err}")


if __name__ == "__main__":
    absolute_path = join(Path().absolute(), "")
    verify_virtual_env(join(absolute_path, "bin", "pip"))

    path_to_download = join(absolute_path, "dmyk", "source", "download")
    copy_external_modules(
        absolute_path=absolute_path,
        directories=(("pytube", path_to_download),),
    )
