# Global imports
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from typing import Type

# Local imports

from pytube import Playlist
from .interfaces import DownloadPlaylistInterface, DownloadEssentialInterface
from .message import Message
from source_notification import NotificationInterface

class DownloadPlaylist(DownloadPlaylistInterface):
    def __init__(self, link: str, mp3: bool, \
        notification_obj: Type[NotificationInterface]) -> None:

        self.__playlist = Playlist(link)
        self.__CONVERT = mp3
        self.__notification_obj = notification_obj

    def download_playlist(self, download : Type[DownloadEssentialInterface]):
        Message.set_output(f"Download da playlist iniciado!")
        self.__notification_obj.send_notification(
            title='DMYK',
            description='Download da playlist iniciado!',
            duration=3
        )
        for video in self.__playlist:
            if self.__CONVERT:
                download(
                    video, 
                    self.__CONVERT, 
                    self.__notification_obj
                ).download_audio()
            else:
                download(
                    video, 
                    self.__CONVERT, 
                    self.__notification_obj
                ).download_video()
        Message.set_output("Download da Playlist concluído!")
        self.__notification_obj.send_notification(
            title='DMYK',
            description='Download da Playlist concluído!',
            duration=3
        )