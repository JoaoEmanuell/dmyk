# Global imports
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from ..youtube_dl.YoutubeDL import YoutubeDL

from ..interfaces import (
    DownloadPlaylistInterface,
    DownloadEssentialInterface,
    DownloadVideoInterface,
)
from source.utils import MessageInterface


class YoutubeDLDownloadPlaylist(DownloadPlaylistInterface):
    def __init__(
        self,
        link: str,
        mp3: bool,
        quality: str,
        message: MessageInterface,
        download_essential: DownloadEssentialInterface,
    ) -> None:
        self.__playlist = link
        self.__CONVERT = mp3
        self.__quality = quality
        self.__message = message
        self.__download_essential = download_essential

    def download_playlist(self, download: DownloadVideoInterface):
        self.__message.set_out("Coletando dados da playlist!")
        playlist_videos = self.__get_playlist_urls()
        self.__message.set_out(f"Download da playlist iniciado!")
        for video in playlist_videos:
            download(
                link=video,
                mp3=self.__CONVERT,
                quality=self.__quality,
                message=self.__message,
                download_essential=self.__download_essential,
            ).download()
        self.__message.set_out("Download da Playlist concluído!")

    def __get_playlist_urls(self) -> list:
        ydl_opts = {"quiet": True, "no_warnings": True, "extract_flat": "in_playlist"}
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.__playlist, download=False)
            playlist_urls = [
                f"https://youtube.com/watch/?v={entry['url']}"
                for entry in info_dict["entries"]
            ]

        return playlist_urls
