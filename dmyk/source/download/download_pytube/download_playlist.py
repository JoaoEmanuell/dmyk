# Global imports
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Local imports

from ..pytube import Playlist
from ..interfaces import (
    DownloadPlaylistInterface,
    DownloadEssentialInterface,
    DownloadVideoInterface,
)
from source.utils import MessageInterface


class DownloadPlaylist(DownloadPlaylistInterface):
    def __init__(
        self,
        link: list,
        mp3: bool,
        quality: str,
        message: MessageInterface,
        download_essential: DownloadEssentialInterface,
    ) -> None:
        self.__playlist: list[str] = Playlist(link)
        self.__CONVERT = mp3
        self.__quality = quality
        self.__message = message
        self.__download_essential = download_essential

    def download_playlist(self, download: DownloadVideoInterface):
        self.__message.set_out(f"Download da playlist iniciado!")
        for video in self.__playlist:
            download(
                link=video,
                mp3=self.__CONVERT,
                quality=self.__quality,
                message=self.__message,
                download_essential=self.__download_essential,
            ).download()
        self.__message.set_out("Download da Playlist concluído!")
