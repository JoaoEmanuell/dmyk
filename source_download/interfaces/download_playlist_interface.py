from abc import ABC, abstractmethod
from typing import Type

from source_notification import NotificationInterface

class DownloadPlaylistInterface(ABC):
    @abstractmethod
    def __init__(self, link : str, mp3 : bool, \
        notification_obj: Type[NotificationInterface]) -> None:
        raise NotImplementedError

    @abstractmethod
    def download_playlist(self) -> None:
        raise NotImplementedError