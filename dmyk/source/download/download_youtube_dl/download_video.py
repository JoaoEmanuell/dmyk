# Global imports

# Create ssl
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from ..youtube_dl.YoutubeDL import YoutubeDL
from ..interfaces import (
    DownloadVideoInterface,
    DownloadEssentialInterface,
)
from source.utils import MessageInterface


class YoutubeDlDownloadVideo(DownloadVideoInterface):
    def __init__(
        self,
        link: str,
        mp3: bool,
        quality: str,
        message: MessageInterface,
        download_essential: DownloadEssentialInterface,
    ) -> None:
        # Manager

        self.__message = message
        self.__download_essential = download_essential
        self.__message.set_pb(100, 0, "indeterminate")
        self.__templates_strings = {
            "start": "Iniciando o download %s \n%s\nAguarde um pouco!",
            "download": "Download %s\n%s\nIniciado",
            "convert": "Música \n%s\nbaixada e convertida para MP3",
            "end": 'Vídeo \n"%s"\n baixado',
            "exists": '%s "%s" já foi baixado!',
        }
        self.__path = self.__download_essential._get_download_path()

        # YoutubeDL

        self.__ydl_opts = {
            "quiet": True,
            "no_warnings": True,
        }

        # Video

        self.__video = self.__format_url(link)
        self.__convert = mp3
        self.__quality = self.__quality_to_itag(quality)

    def download(self) -> None:
        print("Youtube dl download")
        self.__message.set_out("Coletando dados do vídeo!\nAguarde um momento!")
        self.__video_infos = self.__get_video_infos()
        self.__video_form = None
        title = self.__get_title()
        headers = self.__get_headers(self.__quality)

        if self.__convert:
            self.__message.set_out(
                self.__templates_strings["start"] % ("da música", title)
            )
            self.__download_audio()
        else:
            self.__message.set_out(
                self.__templates_strings["start"] % ("do vídeo", title)
            )
            self.__download_video(headers, title)

    def __download_video(self, headers: dict, title: str) -> None:
        video_url = self.__get_video_url(self.__quality)
        self.__download_essential.download_in_parts(
            url=video_url, headers=headers, filename=f"{title}.mp4"
        )
        self.__message.set_out(f"Download do vídeo\n{title}\nFinalizado!")

    def __download_audio(self) -> None:
        pass

    def __format_url(self, url: str) -> str:
        if "short" in url:
            video_id = url.split("/")[4]
            base_url = r"https://www.youtube.com/watch/?v="
            return f"{base_url}{video_id}"
        else:
            return url

    def __quality_to_itag(self, quality: str) -> str:
        itags = {"720p": "22", "360p": "18"}
        if quality in itags:
            return itags[quality]
        else:
            self.__message.set_out(
                "Qualidade indisponível, baixando na melhor qualidade possível!"
            )
            return itags["720p"]

    def __get_video_infos(self) -> dict:
        with YoutubeDL(self.__ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.__video, download=False)
        return info_dict

    def __get_video_url(self, itag: str) -> dict:
        if self.__video_form is not None and self.__video_form["format_id"] == itag:
            return self.__video_form["url"]
        else:
            for form in self.__video_infos["formats"]:
                if form["format_id"] == itag:
                    self.__video_form = form
                    return self.__video_form["url"]

    def __get_title(self) -> str:
        if self.__video_infos != None:
            return self.__video_infos["title"]
        else:
            self.__video_infos = self.__get_video_infos()
            return self.__video_infos["title"]

    def __get_headers(self, itag: str) -> dict:
        if self.__video_form is not None and self.__video_form["format_id"] == str(
            itag
        ):
            return self.__video_form["http_headers"]
        else:
            for form in self.__video_infos["formats"]:
                if form["format_id"] == str(itag):
                    self.__video_form = form
                    return self.__video_form["http_headers"]
