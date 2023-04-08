# Global imports

# Create ssl
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
from os.path import join
from time import sleep

# Local imports

from .pytube import YouTube, Stream
from .interfaces import (
    DownloadVideoInterface,
    DownloadEssentialInterface,
)
from source.utils import MessageInterface


class DownloadVideo(DownloadVideoInterface):
    def __init__(
        self,
        link: str,
        mp3: bool,
        quality: str,
        message: MessageInterface,
        download_essential: DownloadEssentialInterface,
    ) -> None:
        self.__video = YouTube(link, on_progress_callback=progress)
        self.__convert = mp3
        self.__quality = quality
        self.__message = message
        self.__download_essential = download_essential
        self.__message.set_pb(100, 0)

        self.__templates_strings = {
            "start": "Iniciando o download %s \n%s\nAguarde um pouco!",
            "download": "Download %s\n%s\nIniciado",
            "convert": "Música \n%s\nbaixada e convertida para MP3",
            "end": 'Vídeo \n"%s"\n baixado',
            "exists": '%s "%s" já foi baixado!',
        }

        self.__path = self.__download_essential._get_download_path()

    def private__download_vídeo(self) -> None:
        self.__message.set_out(
            self.__templates_strings["start"] % ("do vídeo", self.__video.title)
        )

        self.__stream = self.__video.streams.get_by_resolution(self.__quality)

        if self.__stream == None:
            self.__message.set_out(
                f"Qualidade {self.__quality} não está disponível!\n Iniciando download na maior qualidade possível!"
            )
            sleep(1.5)
            self.__stream = self.__video.streams.get_highest_resolution()

        if self.__download_essential.verify_if_file_not_exists(
            self.__convert, self.__stream, self.__path
        ):

            self.__message.set_out(
                self.__templates_strings["download"] % ("do vídeo", self.__video.title)
            )
            self.__stream.download(output_path=f"{self.__path}/Música/")
            self.__message.set_out(
                self.__templates_strings["end"] % (self.__video.title)
            )
            self.__message.set_pb(100, 100)
        else:
            self.__message.set_out(
                self.__templates_strings["exists"] % ("Vídeo", self.__video.title)
            )

    def private_download_audio(self) -> None:
        self.__message.set_out(
            self.__templates_strings["start"] % ("da música", self.__video.title)
        )

        self.__stream = self.__video.streams.get_audio_only()

        if self.__download_essential.verify_if_file_not_exists(
            self.__convert, self.__stream, self.__path
        ):

            self.__message.set_out(
                self.__templates_strings["download"] % ("da música", self.__video.title)
            )
            self.__stream.download(output_path=join(self.__path, "", "Música", ""))
            self.__message.set_pb(100, 100)
            self.__message.set_out("Iniciando conversão para mp3, aguarde um pouco!")
            filename = str(self.__stream.default_filename)

            try:
                path_to_music = join(self.__path, "", "Música", filename)
                self.__download_essential.convert_to_mp3(
                    path_to_music, self.__stream.default_filename
                )
            except Exception as err:
                self.__message.set_out(
                    f"Ocorreu um erro durante a conversão\nO vídeo não pode ser convertido mas ele já está salvo na pasta música!"
                )
                print(f"ERR: {err.with_traceback()}")

            else:

                self.__message.set_pb(100, 100)

                self.__message.set_out(
                    self.__templates_strings["convert"] % (self.__video.title)
                )

        else:

            self.__message.set_out(
                self.__templates_strings["exists"] % ("Música", self.__video.title)
            )

    def download(self) -> None:
        if self.__convert:
            self.private_download_audio()
        else:
            self.private__download_vídeo()


def progress(stream: Stream, chunk: bytes, bytes_remaining: int) -> None:
    """from .pytube.cli"""
    from .message import Message

    bytes_remaining = bytes_remaining // 1048576
    filesize = stream.filesize // 1048576
    complete = filesize - bytes_remaining
    if bytes_remaining != 0:
        Message.set_pb(filesize, complete)
