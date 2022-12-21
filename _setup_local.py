from os.path import exists, join
from os import mkdir, listdir
from shutil import copytree
from pathlib import Path
from typing import Tuple


def verify_virtual_env(path: str) -> bool:
    if exists(path):
        return True
    raise FileNotFoundError("VIRTUAL ENV NOT FOUND!")


def copy_external_modules(
    absolute_path: str, new_directory: str, directories: Tuple[str]
) -> bool:
    external_modules_directory = join(absolute_path, new_directory, "external_modules")

    if not exists(external_modules_directory):
        print(f"Mkdir : {external_modules_directory}")
        mkdir(external_modules_directory)

    path_to_directory_packages = join(
        absolute_path, "lib", listdir(f"{absolute_path}lib")[0], "site-packages", ""
    )

    print(f"Python packages : {path_to_directory_packages}")
    external_modules_path = join(absolute_path, new_directory)
    print(f"Path to external: {external_modules_path}")

    for directory in directories:

        path = join(path_to_directory_packages, directory, "")

        try:
            copytree(path, join(external_modules_path, directory), False, None)
            print(f"Package {directory} copied with success")
        except FileNotFoundError:
            print(f"Package not found : {directory}")
        except FileExistsError:
            print(f"Exists : {directory}")
        except Exception as err:
            print(f"ERR : {err}")


if __name__ == "__main__":
    absolute_path = join(Path().absolute(), "")
    verify_virtual_env(join(absolute_path, "bin", "pip"))
    copy_external_modules(
        absolute_path=absolute_path,
        new_directory=join("dmyk", "source", "download"),
        directories=("pytube",),
    )
