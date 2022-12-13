# Global imports
from threading import Thread
from urllib.error import URLError
from urllib.request import urlopen

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.utils import platform

# Local imports
from intent import Intent # Android intent
from source_android import Android, service
from source_api import ApiControl
from source_ui import ui_drop_down_obj

from source_download import (
    DownloadVideo, DownloadPlaylist, Message, MessageInterface
)
from download import DownloadVerify

class Tela(Screen):
    def __init__(self, message_class: MessageInterface, **kwargs):
        super().__init__(**kwargs)
        self.ids.link.text = Intent(platform).get_intent_text()
        self.__message_class = message_class
        ApiControl()

    def main(self) -> None:
        try :
            urlopen('https://www.youtube.com')
        except URLError:
            self.__message_class.set_output('Sua conexão de internet está \
                indisponível, por favor tente novamente')
        else:
            self.start_download()

    def start_download(self):
        self.__message_class.set_output('')
        self.ids.progressbar.value = 0
        quality = ui_drop_down_obj.get_text()
        try:
            url = str(self.ids.link.text)

            Thread(
                target=DownloadVerify.main, 
                args=(url, self.verify_mp3(), DownloadVideo, DownloadPlaylist)
            ).start()

        except Exception as erro:
            self.__message_class.set_output(f'Alguma coisa deu errado!\nPor favor \
                insira uma nova url\nTente novamente!\n {erro}')

    def verify_mp3(self) -> bool:
        mp3 = self.ids.mp3.state
        mp4 = self.ids.mp4.state
        if mp3 == 'down':
            return True
        elif mp4 == 'down' :
            return False
        else:
            return True

    def show_drop_down(self) -> None:
        ui_drop_down_obj.open(self.ids.mp4)
        self.ids.mp4.state = 'down'

class Main(App):
    def build(self) -> Screen:
        return Tela(Message)

    def on_start(self): service.start_service()

    def on_stop(self): service.stop_service()

    def on_pause(self): return True

    def on_resume(self): pass

if __name__ == '__main__':
    Android()
    Main().run()