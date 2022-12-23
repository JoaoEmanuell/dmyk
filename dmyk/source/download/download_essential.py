# Global imports
from os.path import exists, isdir, join
from os import mkdir, remove, rename
from re import sub
from getpass import getuser
from time import sleep

from kivy.utils import platform

# Local imports

from .interfaces import DownloadEssentialInterface
from ..api import ApiControlInterface
from .interfaces.download_content_interface import DownloadContentInterface
from .interfaces.message_interface import MessageInterface
from .pytube.streams import Stream


class DownloadEssential(DownloadEssentialInterface):
    def __init__(
        self,
        api_control: ApiControlInterface,
        download_content: DownloadContentInterface,
        message: MessageInterface,
    ) -> None:
        self.__api_control = api_control
        self.__download_content = download_content
        self.__message = message

    def verify_if_file_not_exists(self, convert: bool, file: Stream, path: str) -> bool:
        if convert:

            filename = str(file.default_filename)
            filename = filename.replace(".mp4", ".mp3")  # Remove .mp4 extension
            filename = sub(r"(\s\s)", " ", filename)  # Remove double spaces

            return not (exists(f"{path}Música/{filename}"))
        else:
            filename = file.default_filename
            return not (exists(f"{path}Música/{filename}"))

    def convert_to_mp3(self, file_path: str, file_name: str) -> None:

        rename(file_path, file_path.replace(".mp4", ".mp3"))
        file_path = file_path.replace(".mp4", ".mp3")

        # Upload file
        print("Upload file")
        self.__message.set_out("Iniciando conversão para mp3, aguarde um pouco!")
        response = self.__api_control.upload(file_path)
        hash = response["hash"]
        self.__message.set_out("Conversão iniciada!")
        self.__message.set_pb(0, 100)
        print(f"Hash: {hash}")
        sleep(2)

        while True:
            # Monitoring conversion status
            sleep(2)
            response = self.__api_control.get_status(hash)
            print(f"Status: {response}")
            if response["status"]:  # status == True
                break
            try:
                self.__message.set_pb(response["total"], response["current"])
            except KeyError:
                pass

        # Set progress to max

        self.__message.set_pb(1, 1)

        # Download File

        converted = self.__api_control.get_file(hash)
        print(f"Converted: {converted}")
        self.__message.set_out("Removendo arquivo antigo")
        remove(file_path)
        self.__message.set_out("Download do arquivo convertido iniciado!")
        file = self.__download_content.download(converted["audio"], self.__message)

        # Save File

        self.__message.set_out("Salvando novo arquivo")
        path = join(self._get_download_path(), "Música")
        print(path)
        filename = file_name.replace(".mp4", ".mp3")  # Remove .mp4 extension
        filename = sub(r"(\s\s)", " ", filename)  # Remove double spaces

        self.__download_content.save_file(name=filename, dir=path, content=file)

        # Delete file on server
        self.__api_control.delete_file(hash)

    def _get_download_path(self) -> str:
        paths = {
            "win": r"C:\Users\%s\Desktop\\",
            "linux": "/home/%s",
            "android": "/storage/emulated/0",
        }
        try:
            if platform != "android":
                return paths[platform] % getuser()
            return paths[platform]
        except KeyError:
            raise "Plataforma invalida"

    def create_directory(self, name: str) -> None:
        path = self._get_download_path()
        print(f"Path: {path}")
        if not (isdir(f"{path}/{name}")):
            path = join(path, name)
            mkdir(path)
