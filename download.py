# Global imports

from re import findall
from typing import Type

# Local imports

from source_download import (
    DownloadEssential, DownloadEssentialInterface, DownloadPlaylistInterface, 
    Message
)
from source_notification import notification

class DownloadVerify:

    def verify_url(url: str) -> bool:
        verify_tuple_regex = (
            r'^(https:\/\/www.youtube.com\/)', # domain full
            r'^(https:\/\/youtu.be\/)', # domain short
        )

        for verify in verify_tuple_regex:
            if len(findall(verify, str(url))) != 0: 
                return True # Verify regex

        return False

    def verify_playlist(url: str) -> bool:
        verify_url = findall(r'(playlist\?list=)', str(url))
        if len(verify_url) != 0 :
            return True
        else :
            return False
    
    def main(link:str, mp3:bool, \
        video: Type[DownloadEssentialInterface], \
        playlist: Type[DownloadPlaylistInterface]) -> None:

        link = str(link)
        print("Iniciando o download")
        notification.send_notification()
        try :
            if DownloadVerify.verify_url(link):
                DownloadEssential().create_directory('Música')
                if DownloadVerify.verify_playlist(link):
                    print("Verificado playlist, iniciando o download da playlist")
                    playlist(link, mp3, notification).download_playlist(video)
                else :
                    print("Verificado vídeo!")
                    if mp3:
                        print("Iniciando download da música")
                        video(link, mp3, notification).download_audio()
                    else :
                        print("Iniciando download do vídeo")
                        video(link, mp3, notification).download_video()
            else:
                Message.set_output("Erro, url invalida!")

        except Exception as Ex :
            Message.set_output("YouTube quebrou o app :/")
            print(f'ERROR:{Ex.with_traceback()}')