# Global imports

from re import findall

# Local imports

from .interfaces import (
    DownloadEssentialInterface,
    DownloadPlaylistInterface,
    DownloadVideoInterface,
    DownloadManagerInterface,
)
from source.utils import MessageInterface


class DownloadManager(DownloadManagerInterface):
    def __init__(
        self,
        link: str,
        mp3: bool,
        quality: str,
        video: list[DownloadVideoInterface],
        playlist: list[DownloadPlaylistInterface],
        message: MessageInterface,
        download_essential: DownloadEssentialInterface,
    ) -> None:
        self.__link = str(link)
        self.__mp3 = bool(mp3)
        self.__quality = str(quality)

        self.__video = video
        self.__playlist = playlist
        self.__download_essential = download_essential
        self.__message = message
        self.__downloader_number = 0  # Downloader to use

        self.main()

    def private__verify_url(self) -> bool:
        """Verify if is a YouTube url"""
        verify_tuple_regex = (
            r"^(https:\/\/www.youtube.com\/)",  # domain full
            r"^(https:\/\/youtu.be\/)",  # domain short
            r"^(https:\/\/youtube.com\/)",  # other domain [playlist shared]
        )

        for verify in verify_tuple_regex:
            if len(findall(verify, self.__link)) != 0:
                return True  # Verify regex

        return False

    def private__verify_playlist(self) -> bool:
        """Verify if is a playlist url"""
        verify_url = findall(r"(playlist\?list=)", self.__link)
        if len(verify_url) != 0:
            return True
        else:
            return False

    def main(self) -> None:
        print("Iniciando o download")
        self.set_dbt_style("stop")
        try:
            download_args_dict = {
                "link": self.__link,
                "mp3": self.__mp3,
                "quality": self.__quality,
                "message": self.__message,
                "download_essential": self.__download_essential,
            }

            video_downloader = self.__video[self.__downloader_number]
            playlist_downloader = self.__playlist[self.__downloader_number]

            if self.private__verify_url():
                self.__download_essential.create_directory("Música")
                if self.private__verify_playlist():
                    print("Verificado playlist, iniciando o download da playlist")
                    playlist_downloader(**download_args_dict).download_playlist(
                        video_downloader
                    )
                else:
                    print("Verificado vídeo!")
                    self.set_dbt_style("stop")
                    print("Iniciando download do vídeo")
                    video_downloader(**download_args_dict).download()
                    self.set_dbt_style()
            else:
                self.__message.set_out("Erro, url invalida!")
                self.set_dbt_style()

        except Exception as Ex:
            if self.__downloader_number < (len(self.__video) - 1):
                self.__message.set_out(
                    f"Erro no método de download {self.__downloader_number}!\nTentando por outro método!"
                )

                self.__downloader_number += 1

                print(f"ERROR DOWNLOADER {self.__downloader_number}: {Ex}")
                self.main()
            else:
                self.__message.set_out("YouTube quebrou o app:/")
                self.set_dbt_style()
                self.__message.set_pb(0, 0)
                print(f"ERROR: {Ex.with_traceback()}")

    def set_dbt_style(self, background_style: str = "default") -> None:
        self.__message.set_ws("download_button", background_style)
