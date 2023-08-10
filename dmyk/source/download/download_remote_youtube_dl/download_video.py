from requests import post

from ..interfaces import (
    DownloadVideoInterface,
    DownloadEssentialInterface,
)
from source.utils import MessageInterface
from ..interfaces import DownloadVideoInterface

class DownloadRemoteVideoYoutubeDl(DownloadVideoInterface):
    def __init__(self, link: str, mp3: bool, quality: str, message: MessageInterface, download_essential: DownloadEssentialInterface) -> None:
        self.__endpoint = "https://youtubedlapi-apolomundogames3.b4a.run/api/video/"
        self.__url = link
        self.__mp3 = mp3
        self.__quality = quality
        self.__message = message
        self.__download_essential = download_essential
        self.__templates_strings = {
            "start": "Iniciando o download %s \n%s\nAguarde um pouco!",
            "download": "Download %s\n%s\nIniciado",
            "convert": "Música \n%s\nbaixada e convertida para MP3",
            "end": 'Vídeo \n"%s"\n baixado',
            "exists": '%s "%s" já foi baixado!',
        }
        self.__message.set_pb(100, 0, "indeterminate")
    
    def download(self) -> None:
        if self.__mp3:
            self.__message.set_out("Coletando dados da música\nAguarde um pouco!")
            self.__download_audio()
        else:
            self.__message.set_out("Coletando dados do vídeo\nAguarde um pouco!")
            self.__download_video()
            
    def __download_audio(self) -> None:
        data = {
            "url": self.__url,
            "quality": "mp3"
        }
        request = post(self.__endpoint, data=data)
        json = request.json()
        filename = f'{json["title"]}.mp3'
        headers = json["headers"]
        video_url = json["url"]
        title = json["title"]
        self.__message.set_out(
            self.__templates_strings["download"] % ("da música", title)
        )
        self.__download_essential.download_in_parts(
            url=video_url, headers=headers, filename=filename
        )
        self.__message.set_out("Iniciando conversão para mp3, aguarde um pouco!")
        path_to_file = (
            f"{self.__download_essential._get_download_path()}/Música/{filename}"
        )
        self.__download_essential.convert_to_mp3(
            file_path=path_to_file, file_name=f"{filename}"
        )
        self.__message.set_out(self.__templates_strings["convert"] % title)
    
    def __download_video(self) -> None:
        data = {
            "url": self.__url,
            "quality": self.__quality
        }
        request = post(self.__endpoint, data=data)
        json = request.json()
        filename = f'{json["title"]}.mp4'
        headers = json["headers"]
        video_url = json["url"]
        title = json["title"]
        self.__message.set_out(
            self.__templates_strings["download"] % ("do vídeo", title)
        )
        self.__download_essential.download_in_parts(
            url=video_url, headers=headers, filename=filename
        )
        print("End download")
        self.__message.set_out(self.__templates_strings["end"] % (title))