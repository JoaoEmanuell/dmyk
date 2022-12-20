from abc import ABC, abstractclassmethod


class DownloadManagerInterface(ABC):
    @abstractclassmethod
    def verify_url(cls, url: str) -> bool:
        """Verify url, validate if is a YouTube url

        Args:
            url (str): url

        Returns:
            bool: True if url is valid
        """
        raise NotImplementedError()

    @abstractclassmethod
    def verify_playlist(cls, url: str) -> bool:
        """Verify playlist url

        Args:
            url (str): url

        Returns:
            bool: True if url is a playlist url
        """
        raise NotImplementedError()
