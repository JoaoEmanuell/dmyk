from abc import ABC, abstractmethod

from .download_video_interface import DownloadVideoInterface
from .download_playlist_interface import DownloadPlaylistInterface
from .message_interface import MessageInterface
from .download_essential_interface import DownloadEssentialInterface


class DownloadManagerInterface(ABC):
    @abstractmethod
    def __init__(
        self,
        link: str,
        mp3: bool,
        quality: str,
        video: DownloadVideoInterface,
        playlist: DownloadPlaylistInterface,
        message: MessageInterface,
        download_essential: DownloadEssentialInterface,
    ) -> None:
        """Init

        Args:
            link (str): Link to vídeo or music
            mp3 (bool): Mp3 conversion
            quality (str): Quality from vídeo
            video (DownloadVideoInterface): Class Vídeo Download
            playlist (DownloadPlaylistInterface): Class playlist Download
            message (MessageInterface): Class Message
            download_essential (DownloadEssentialInterface): Class Download Essential
        """
        raise NotImplementedError()

    @abstractmethod
    def main(self) -> None:
        """
        Make verifications and start download or give an alert informing if
        url is invalid
        """
        raise NotImplementedError()
