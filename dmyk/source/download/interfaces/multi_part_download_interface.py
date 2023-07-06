from abc import ABC, abstractmethod

from source.thread import MultiThreadInterface, CustomThreadInterface


class MultiPartDownloadInterface(ABC):
    @abstractmethod
    def __init__(
        self,
        part_number: int,
        multi_thread: MultiThreadInterface,
        custom_thread: CustomThreadInterface,
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    def download(self, url: str, headers: dict) -> None:
        raise NotImplementedError()
