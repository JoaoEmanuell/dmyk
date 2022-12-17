# Global imports

from re import findall
from typing import Type

# Local imports

from .message import Message
from .download_essential import DownloadEssential
from ..interfaces import DownloadEssentialInterface, DownloadPlaylistInterface

class DownloadManager:
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

        print("Iniciando o download")
        link = str(link)
        try:
            if DownloadManager.verify_url(link):
                DownloadEssential.create_directory('Música')
                if DownloadManager.verify_playlist(link):
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
                        cls.set_dbt_style_text()
                    else:
                        Message.set_widget_style(
                            'download_button', 'background_color', 'stop'
                        )
                        print("Iniciando download do vídeo")
                        video(link, mp3, quality).download_video()
                        cls.set_dbt_style_text()
            else:
                Message.set_out("Erro, url invalida!")
                cls.set_dbt_style_text()

        except Exception as Ex:
            Message.set_out("YouTube quebrou o app:/")
            cls.set_dbt_style_text()
            print(f'ERROR:{Ex.with_traceback()}')

    @classmethod
    def set_dbt_style_text(cls, background_style: str='default') -> None:
        Message.set_dbt('Baixar Música ou playlist')
        Message.set_ws('download_button', 'background_color', background_style)