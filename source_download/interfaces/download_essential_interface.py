from abc import ABC, abstractmethod
from typing import Type

from source_notification import NotificationInterface

class DownloadEssentialInterface(ABC):
    @abstractmethod
    def __init__(self, link : str, mp3 : bool, \
        notification_obj: Type[NotificationInterface]) -> None:
        raise NotImplementedError

    @abstractmethod
    def download_video(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def download_audio(self) -> None:
        raise NotImplementedError