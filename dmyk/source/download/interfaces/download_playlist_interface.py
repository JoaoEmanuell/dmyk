from abc import ABC, abstractmethod

from source.utils import MessageInterface
from .download_essential_interface import DownloadEssentialInterface
from .download_video_interface import DownloadVideoInterface


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
    def download_playlist(self, download: DownloadVideoInterface):
        """Start download playlist

        Args:
            download (DownloadVideoInterface): Downloader to download the videos
        """        
        raise NotImplementedError
