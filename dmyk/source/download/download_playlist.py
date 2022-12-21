# Global imports
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Local imports

from .pytube import Playlist
from .interfaces import (
    DownloadPlaylistInterface,
    DownloadEssentialInterface,
    MessageInterface,
    DownloadVideoInterface,
)


class DownloadPlaylist(DownloadPlaylistInterface):
    def __init__(
        self,
        playlist_link: list,
        convert_to_mp3: bool,
        quality: str,
        message: MessageInterface,
        download_essential: DownloadEssentialInterface,
    ) -> None:
        self.__playlist = Playlist(playlist_link)
        self.__CONVERT = convert_to_mp3
        self.__quality = quality
        self.__message = message
        self.__download_essential = download_essential

    def download_playlist(self, download: DownloadVideoInterface):
        self.__message.set_out(f"Download da playlist iniciado!")
        for video in self.__playlist:
            if self.__CONVERT:
                download(video, self.__CONVERT, self.__quality).download_audio()
            else:
                download(video, self.__CONVERT, self.__quality).download_video()
        self.__message.set_out("Download da Playlist concluído!")
