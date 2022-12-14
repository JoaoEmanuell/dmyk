from abc import ABC, abstractclassmethod

class DownloadInterface(ABC) :

    @abstractclassmethod
    def download(cls, url: str) -> bytes :
        raise NotImplementedError

    @abstractclassmethod
    def save_file(cls, name: str, path: str, content: bytes) -> None :
        raise NotImplementedError