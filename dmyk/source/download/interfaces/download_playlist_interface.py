from abc import ABC, abstractmethod

from .message_interface import MessageInterface
from .download_essential_interface import DownloadEssentialInterface


class DownloadPlaylistInterface(ABC):
    @abstractmethod
    def __init__(
        self,
        link: str,
        mp3: bool,
        quality: str,
        message: MessageInterface,
        download_essential: DownloadEssentialInterface,
    ) -> None:
        """Init

        Args:
            link (str): link to YouTube vídeo
            mp3 (bool): convert vídeo
            quality (str): quality of download
            message (MessageInterface): message class to send message for interface
            download_essential (DownloadEssentialInterface): download essential object
        """
        raise NotImplementedError

    @abstractmethod
    def download_playlist(self) -> None:
        """Start download playlist"""
        raise NotImplementedError
