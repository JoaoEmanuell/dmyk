# Global imports

# Create ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from os.path import join
from typing import Type

# Local imports

from pytube import YouTube
from pytube.cli import on_progress
from .download_essential import DownloadEssential
from .interfaces import DownloadEssentialInterface
from .message import Message
from source_notification import NotificationInterface

class DownloadVideo(DownloadEssentialInterface):
    def __init__(self, link: str, mp3: bool, notification_obj: Type[NotificationInterface]) -> None:
        self.__video = YouTube(link, on_progress_callback=on_progress)
        self.__convert = mp3
        self.__notification_obj = notification_obj
        Message.set_progressbar(100, 0)

        self.__templates_strings = {
            'start' : 'Iniciando o download %s \n%s\nAguarde um pouco!',
            'download' : 'Download %s\n"%s"\nIniciado',
            'convert' : 'Música \n%s\nbaixada e convertida para MP3',
            'end' : 'Vídeo \n"%s"\n baixado',
            'exists' : '%s "%s" já foi baixado!'
        }

        self.__path = DownloadEssential._get_download_path()

    def download_video(self) -> None:
        Message.set_output(self.__templates_strings['start'] % ('do vídeo', self.__video.title))

        self.__stream = self.__video.streams.get_highest_resolution()

        if DownloadEssential.verify_if_file_not_exists(self.__convert, self.__stream, self.__path):

            Message.set_output(self.__templates_strings['download'] % ('do vídeo', self.__video.title))

            self.__notification_obj.send_notification(
                description=self.__templates_strings['download'] \
                    % ('do vídeo', self.__video.title),
            )

            self.__stream.download(output_path=f'{self.__path}/Música/') # Start download

            Message.set_output(self.__templates_strings['end'] % (self.__video.title))

            self.__notification_obj.send_notification(
                description=self.__templates_strings['end'] % (self.__video.title),
            )

            Message.set_progressbar(100, 100)
        else :
            Message.set_output(self.__templates_strings['exists'] % ('Vídeo', self.__video.title))

    def download_audio(self) -> None:
        Message.set_output(self.__templates_strings['start'] % ('da música', self.__video.title))

        self.__notification_obj.send_notification(
            description=self.__templates_strings['start'] \
                % ('da música', self.__video.title),
        )

        self.__stream = self.__video.streams.get_audio_only() # Start download

        if DownloadEssential.verify_if_file_not_exists(self.__convert, self.__stream, self.__path):

            Message.set_output(self.__templates_strings['download'] % ('da música', self.__video.title))
            self.__stream.download(output_path=join(self.__path, '', 'Música', ''))
            Message.set_progressbar(100, 100)
            Message.set_output('Iniciando conversão para mp3, aguarde um pouco!')

            self.__notification_obj.send_notification(
                description='Iniciando conversão para mp3',
            )

            filename = str(self.__stream.default_filename)

            try : 
                path_to_music = join(self.__path, '', 'Música', filename)
                DownloadEssential.convert_to_mp3(
                    path_to_music, self.__stream.default_filename
                )
            except Exception as err:
                Message.set_output(f'Ocorreu um erro durante a conversão\nO vídeo não pode ser convertido mas ele já está salvo na pasta música!')

                self.__notification_obj.send_notification(
                    description='Erro durante a conversão!',
                )

                print(f'ERR: {err.with_traceback()}')
            
            else :

                Message.set_progressbar(100, 100)

                Message.set_output(self.__templates_strings['convert'] % (self.__video.title))

                self.__notification_obj.send_notification(
                    description=self.__templates_strings['convert'] \
                        % (self.__video.title),
                )

        else :

            Message.set_output(self.__templates_strings['exists'] % ('Música', self.__video.title))
