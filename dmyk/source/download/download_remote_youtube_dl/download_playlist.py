from requests import post

from ..interfaces import (
    DownloadVideoInterface,
    DownloadEssentialInterface,
    DownloadPlaylistInterface,
)
from source.utils import MessageInterface


class DownloadRemotePlaylistYoutubeDl(DownloadPlaylistInterface):
    def __init__(
        self,
        link: str,
        mp3: bool,
        quality: str,
        message: MessageInterface,
        download_essential: DownloadEssentialInterface,
    ) -> None:
        self.__endpoint = "https://youtubedlapi-apolomundogames3.b4a.run/api/playlist/"
        self.__url = link
        self.__mp3 = mp3
        self.__quality = quality
        self.__message = message
        self.__download_essential = download_essential
        self.__retry = 0

    def download_playlist(self, download: DownloadVideoInterface):
        try:
            self.__message.set_out("Coletando dados da playlist!")
            data = {"url": self.__url}
            request = post(self.__endpoint, data=data, timeout=60)
            playlist_videos = request.json()
        except Exception:
            if self.__retry == 3:
                raise Exception("Erro to download playlist!")
            else:
                self.download_playlist(download)
                self.__retry += 1
        else:
            self.__message.set_out(f"Download da playlist iniciado!")
            for video in playlist_videos:
                download(
                    link=video,
                    mp3=self.__mp3,
                    quality=self.__quality,
                    message=self.__message,
                    download_essential=self.__download_essential,
                ).download()
            self.__message.set_out("Download da Playlist concluído!")
