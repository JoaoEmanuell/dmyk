from os.path import exists, join, basename
from os import listdir, system, mkdir, remove
from shutil import copytree
from pathlib import Path
from typing import Tuple
from sys import version
from re import search, compile, sub
from io import BytesIO
from urllib.request import Request, urlopen


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


def download_save(url: str, save_path: str, name: str) -> None:
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with urlopen(request) as response:
        file: bytes = b""
        length = response.getheader("content-Length")
        block_size = 1000000  # 1MB Default

        if length:
            length = int(length)
            block_size = max(4096, length // 20)

        buffer_all = BytesIO()
        size = 0

        print("Start Download!")

        while True:
            buffer_now = response.read(block_size)
            file += buffer_now

            if not buffer_now:
                break

            buffer_all.write(buffer_now)
            size += len(buffer_now)

            if length:
                percent = int((size / length) * 100)
                print(f"{percent}%", end=" ")

    print()
    if not exists(save_path):
        mkdir(save_path)

    with open(join(save_path, name), "wb") as f:
        f.write(file)


def extract_module(path_to_file: str, path_to_save: str) -> None:
    # Install dependencies
    print("Start extract module!")
    print("Install dependencies")

    system("pip install pip-autoremove==0.10.0")
    system("pip install py7zr==0.20.2")

    print("Dependencies installed")
    print("Start extract file")
    from py7zr import SevenZipFile  # type: ignore

    with SevenZipFile(path_to_file, mode="r") as zip:
        zip.extractall(path_to_save)

    print("Finished extract")

    # Delete 7z

    res = input(f"Delete {basename(path_to_file)}? [S/N] ").strip().upper()[0]
    if res == "S":
        remove(path_to_file)

    # Uninstall dependencies
    print("Uninstall dependencies")

    system("pip-autoremove py7zr -y")
    system("pip uninstall pip-autoremove -y")


if __name__ == "__main__":
    absolute_path = join(Path().absolute(), "")
    tmp_path = join(absolute_path, "tmp")
    path_to_download = join(absolute_path, "dmyk", "source", "download")

    verify_virtual_env(join(absolute_path, "bin", "pip"))

    pytube_7z_name = r"pytube.7z"
    download_save(
        url=r"https://github.com/JoaoEmanuell/pytube-dmyk/releases/download/v1.0.0/pytube.7z",
        save_path=tmp_path,
        name=pytube_7z_name,
    )
    extract_module(
        path_to_file=join(tmp_path, pytube_7z_name), path_to_save=path_to_download
    )

    install_kivy(absolute_path)
