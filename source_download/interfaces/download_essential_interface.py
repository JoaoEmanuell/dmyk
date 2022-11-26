from abc import ABC, abstractmethod

class DownloadEssentialInterface(ABC):
    @abstractmethod
    def __init__(self, link : str, mp3 : bool) -> None:
        raise NotImplementedError

    @abstractmethod
    def download_video(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def download_audio(self) -> None:
        raise NotImplementedError