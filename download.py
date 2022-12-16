# Global imports

from re import findall
from typing import Type

# Local imports

from source_download import (
    DownloadEssential, DownloadEssentialInterface, DownloadPlaylistInterface, 
    Message
)

class DownloadVerify:
    @classmethod
    def verify_url(cls, url: str) -> bool:
        verify_tuple_regex = (
            r'^(https:\/\/www.youtube.com\/)', # domain full
            r'^(https:\/\/youtu.be\/)', # domain short
        )

        for verify in verify_tuple_regex:
            if len(findall(verify, str(url))) != 0: 
                return True # Verify regex

        return False

    @classmethod
    def verify_playlist(cls, url: str) -> bool:
        verify_url = findall(r'(playlist\?list=)', str(url))
        if len(verify_url) != 0:
            return True
        else:
            return False
    
    @classmethod
    def main(cls, link: str, mp3: bool, quality: str, \
        video: Type[DownloadEssentialInterface], \
        playlist: Type[DownloadPlaylistInterface]) -> None:

        link = str(link)
        print("Iniciando o download")
        try:
            if DownloadVerify.verify_url(link):
                DownloadEssential.create_directory('Música')
                if DownloadVerify.verify_playlist(link):
                    print("Verificado playlist, iniciando o download da playlist")
                    playlist(link, mp3, quality).download_playlist(video)
                else:
                    print("Verificado vídeo!")
                    if mp3:
                        Message.set_widget_style(
                            'download_button', 'background_color', 'stop'
                        )
                        print("Iniciando download da música")
                        video(link, mp3, quality).download_audio()
                        Message.set_dbt('Baixar Música ou playlist')
                        Message.set_widget_style(
                            'download_button', 'background_color', 'default'
                        )
                    else:
                        Message.set_widget_style(
                            'download_button', 'background_color', 'stop'
                        )
                        print("Iniciando download do vídeo")
                        video(link, mp3, quality).download_video()
                        Message.set_dbt('Baixar Música ou playlist')
                        Message.set_widget_style(
                            'download_button', 'background_color', 'default'
                        )
            else:
                Message.set_out("Erro, url invalida!")
                Message.set_dbt('Baixar Música ou playlist')
                Message.set_ws('download_button', 'background_color', 'default')

        except Exception as Ex:
            Message.set_out("YouTube quebrou o app:/")
            Message.set_dbt('Baixar Música ou playlist')
            print(f'ERROR:{Ex.with_traceback()}')