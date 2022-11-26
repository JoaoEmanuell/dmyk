# Global imports

from pytube import Playlist
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from typing import Type

# Local imports

from .interfaces import DownloadPlaylistInterface, DownloadEssentialInterface
from .message import Message

class DownloadPlaylist(DownloadPlaylistInterface):
    def __init__(self, playlistLink : list, convertToMp3  : bool) -> None:
        self.__playlist = Playlist(playlistLink)
        self.__CONVERT = convertToMp3

    def download_playlist(self, download : Type[DownloadEssentialInterface]):
        Message.set_output(f"Download da playlist iniciado!")
        for video in self.__playlist:
            if self.__CONVERT:
                download(video, self.__CONVERT).download_audio()
            else:
                download(video, self.__CONVERT).download_video()
        Message.set_output("Download da Playlist concluído!")