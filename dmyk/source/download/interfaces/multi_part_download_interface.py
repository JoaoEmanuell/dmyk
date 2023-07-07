from abc import ABC, abstractmethod

from source.thread import MultiThreadInterface, CustomThreadInterface
from source.utils import MessageInterface


class MultiPartDownloadInterface(ABC):
    @abstractmethod
    def __init__(
        self,
        part_number: int,
        multi_thread: MultiThreadInterface,
        custom_thread: CustomThreadInterface,
        message: MessageInterface,
        path: str,
    ) -> None:
        """Init

        Args:
            part_number (int): Number of parts to divide download
            multi_thread (MultiThreadInterface): Multi thread manager class
            custom_thread (CustomThreadInterface): Custom thread manager class
            message (MessageInterface): Message class
            path (str): Path to save file and parts
        """
        raise NotImplementedError()

    @abstractmethod
    def download(self, url: str, headers: dict, filename: str) -> None:
        """Download

        Args:
            url (str): url to download
            headers (dict): Headers to request
            filename (str): Filename to save file
        """
        raise NotImplementedError()
