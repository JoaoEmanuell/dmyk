from abc import ABC, abstractclassmethod

from .message_interface import MessageInterface


class DownloadContentInterface(ABC):
    @abstractclassmethod
    def download(cls, url: str, message: MessageInterface) -> bytes:
        """Download online content

        Args:
            url (str): Url for content
            message (MessageInterface): Message class to send message to interface

        Returns:
            bytes: bytes with content
        """
        raise NotImplementedError

    @abstractclassmethod
    def save_file(cls, name: str, path: str, content: bytes) -> None:
        """Save file

        Args:
            name (str): Name of file
            path (str): Path to save
            content (bytes): Bytes of content
        """
        raise NotImplementedError
