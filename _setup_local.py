from os.path import exists, join
from os import listdir, system
from shutil import copytree
from pathlib import Path
from typing import Tuple
from sys import version
from re import search, compile, sub


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


def install_kivy(absolute_path: str) -> None:
    """Install kivy, used by python3.11 because error on install kivy

    Args:
        absolute_path (str): absolute path to project
    """
    res = input("Kivy is installed? [S/N] ").strip().upper()[0]
    if res == "S":
        pass

    else:

        regex_python_version = compile(
            r"^(\d\.1\d)"
        )  # Original regex: ^(\d\.\1\d\d\.\d), search python 3.1\d
        python_version = search(regex_python_version, version)

        print("Installing Cython")
        system("pip install Cython==0.29.32")
        print("Cython installed with successfully")

        if python_version.span() != None:
            # Thanks for https://github.com/kivy/kivy/issues/8042#issuecomment-1312419599
            print("Install kivy!")
            kivy_install_commands = [
                r"python -m pip install kivy --pre --no-deps --index-url  https://kivy.org/downloads/simple/",
                r'python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/',
            ]
            print("Installing kivy!")
            for kivy_install_command in kivy_install_commands:
                system(kivy_install_command)
            print("Kivy installed")

            print("Remove kivy from requirements.txt")
            new_req = ""
            kivy_regex = compile(
                r"(Kivy\={2}(\d\.){3}dev0\n)"
            )  # Search Kivy==2.2.0.dev0\n
            with open(f"{absolute_path}requirements.txt", "r") as req:
                new_req = req.read()
            with open(f"{absolute_path}requirements.txt", "w") as req:
                req.write(sub(kivy_regex, "", new_req))

        else:
            print("Python version is < 3.11.0, install Kivy using pip install kivy")
            system("pip install Kivy==2.1.0")
            print("Kivy installed")

    res = input("Install requirements.txt? [S/N] ").strip().upper()[0]
    if res == "N":
        return None
    else:
        system(f"pip install -r {absolute_path}requirements.txt")


if __name__ == "__main__":
    absolute_path = join(Path().absolute(), "")
    verify_virtual_env(join(absolute_path, "bin", "pip"))

    path_to_download = join(absolute_path, "dmyk", "source", "download")
    copy_external_modules(
        absolute_path=absolute_path,
        directories=(("pytube", path_to_download),),
    )

    install_kivy(absolute_path)
