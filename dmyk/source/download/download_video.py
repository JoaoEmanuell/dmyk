# Global imports

# Create ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from os.path import join
from time import sleep

# Local imports

from .pytube import YouTube, Stream
from .download_essential import DownloadEssential
from ..interfaces import DownloadEssentialInterface
from .message import Message

class DownloadVideo(DownloadEssentialInterface):
    def __init__(self, link: str, mp3: bool, quality: str) -> None:
        self.__video = YouTube(link, on_progress_callback=progress)
        self.__convert = mp3
        self.__quality = quality
        Message.set_progressbar(100, 0)

        self.__templates_strings = {
            'start': 'Iniciando o download %s \n%s\nAguarde um pouco!',
            'download': 'Download %s\n%s\nIniciado',
            'convert': 'Música \n%s\nbaixada e convertida para MP3',
            'end': 'Vídeo \n"%s"\n baixado',
            'exists': '%s "%s" já foi baixado!'
        }

        self.__path = DownloadEssential._get_download_path()

    def download_video(self) -> None:
        Message.set_output(self.__templates_strings['start'] % ('do vídeo', self.__video.title))
        
        self.__stream = self.__video.streams.get_by_resolution(self.__quality)

        if self.__stream == None:
            Message.set_output(
                f'Qualidade {self.__quality} não está disponível!\n Iniciando download na maior qualidade possível!'
            )
            sleep(1.5)
            self.__stream = self.__video.streams.get_highest_resolution()

        if DownloadEssential.verify_if_file_not_exists(self.__convert, self.__stream, self.__path):

            Message.set_output(self.__templates_strings['download'] % ('do vídeo', self.__video.title))
            self.__stream.download(output_path=f'{self.__path}/Música/')
            Message.set_output(self.__templates_strings['end'] % (self.__video.title))
            Message.set_progressbar(100, 100)
        else:
            Message.set_output(self.__templates_strings['exists'] % ('Vídeo', self.__video.title))

    def download_audio(self) -> None:
        Message.set_output(self.__templates_strings['start'] % ('da música', self.__video.title))

        self.__stream = self.__video.streams.get_audio_only()

        if DownloadEssential.verify_if_file_not_exists(self.__convert, self.__stream, self.__path):

            Message.set_output(self.__templates_strings['download'] % ('da música', self.__video.title))
            self.__stream.download(output_path=join(self.__path, '', 'Música', ''))
            Message.set_progressbar(100, 100)
            Message.set_output('Iniciando conversão para mp3, aguarde um pouco!')
            filename = str(self.__stream.default_filename)

            try: 
                path_to_music = join(self.__path, '', 'Música', filename)
                DownloadEssential.convert_to_mp3(
                    path_to_music, self.__stream.default_filename
                )
            except Exception as err:
                Message.set_output(f'Ocorreu um erro durante a conversão\nO vídeo não pode ser convertido mas ele já está salvo na pasta música!')
                print(f'ERR: {err.with_traceback()}')
            
            else:

                Message.set_progressbar(100, 100)

                Message.set_output(self.__templates_strings['convert'] % (self.__video.title))

        else:

            Message.set_output(self.__templates_strings['exists'] % ('Música', self.__video.title))

def progress(stream: Stream, chunk: bytes, bytes_remaining: int) -> None:
    '''from .pytube.cli'''
    bytes_remaining = bytes_remaining // 1048576
    filesize = stream.filesize // 1048576
    complete = filesize - bytes_remaining
    if bytes_remaining != 0: Message.set_pb(filesize, complete)