# Global imports
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from typing import Type

# Local imports

from pytube import Playlist
from .interfaces import DownloadPlaylistInterface, DownloadEssentialInterface
from .message import Message

class DownloadPlaylist(DownloadPlaylistInterface):
    def __init__(self, playlist_link: list, convert_to_mp3: bool, quality: str) -> None:
        self.__playlist = Playlist(playlist_link)
        self.__CONVERT = convert_to_mp3
        self.__quality = quality

    def download_playlist(self, download: Type[DownloadEssentialInterface]):
        Message.set_output(f"Download da playlist iniciado!")
        for video in self.__playlist:
            if self.__CONVERT:
                download(video, self.__CONVERT, self.__quality).download_audio()
            else:
                download(video, self.__CONVERT, self.__quality).download_video()
        Message.set_output("Download da Playlist concluído!")