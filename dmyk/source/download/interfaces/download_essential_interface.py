from abc import ABC, abstractmethod, abstractclassmethod

from ...api import ApiControlInterface
from .download_content_interface import DownloadContentInterface
from source.utils import MessageInterface
from .multi_part_download_interface import MultiPartDownloadInterface
from ..pytube.streams import Stream


class DownloadEssentialInterface(ABC):
    """Download essential is a class responsible to manager device configs"""

    @abstractmethod
    def __init__(
        self,
        api_control: ApiControlInterface,
        download_content: DownloadContentInterface,
        download_multiple: MultiPartDownloadInterface,
        message: MessageInterface,
    ) -> None:
        """Init

        Args:
            api_control (ApiControlInterface): Api control to manager mp3 api
            download_content (DownloadContentInterface): Download content to download file data and save it
            message (MessageInterface): Class to send messages to application.
        """
        raise NotImplementedError()

    @abstractmethod
    def verify_if_file_not_exists(self, convert: bool, file: Stream, path: str) -> bool:
        """Verify if file not exists

        Args:
            convert (bool): Convert to mp3
            file (Stream): File object
            path (str): Path to save directory

        Returns:
            bool: If exists return true else false
        """
        raise NotImplementedError()

    @abstractmethod
    def convert_to_mp3(self, file_path: str, file_name: str) -> None:
        """Convert audio to mp3 using mp3 api

        Args:
            file_path (str): Absolute file path to save dir
            file_name (str): File name to save audio

        """
        raise NotImplementedError()

    @abstractclassmethod
    def _get_download_path(cls) -> str:
        """Get the download path, where save content

        Returns:
            str: Absolute download path
        """
        raise NotImplementedError()

    @abstractmethod
    def create_directory(self, name: str) -> None:
        """Create a directory on download path

        Args:
            name (str): Name to directory
        """
        raise NotImplementedError()

    @abstractmethod
    def download_in_parts(self, url: str, headers: dict, filename: str) -> None:
        """Download in parts, used to download a file using parts download.

        Args:
            url (str): download file url
            headers (dict): headers to request
            filename (str): Filename to save file
        """
        raise NotImplementedError()
