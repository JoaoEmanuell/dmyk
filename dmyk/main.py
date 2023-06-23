# Global imports
from urllib.error import URLError
from urllib.request import urlopen, Request
from socket import timeout

# from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.utils import platform

# Local imports
from source import (
    Android,
    ApiControl,
    ApiControlInterface,
    CustomThread,
    CustomThreadInterface,
    DownloadContent,
    download_essential,
    DownloadEssentialInterface,
    DownloadManager,
    DownloadManagerInterface,
    PytubeDownloadPlaylist,
    DownloadPlaylistInterface,
    PytubeDownloadVideo,
    DownloadVideoInterface,
    Intent,
    IntentInterface,
    Message,
    MessageInterface,
    service,
    UiDropDown,
    UiDropDownInterface,
    YoutubeDlDownloadVideo,
    YoutubeDLDownloadPlaylist,
    multi_thread,
    MultiThreadInterface,
)
from version import __version__


class Tela(Screen):
    def __init__(
        self,
        message_class: MessageInterface,
        custom_thread: CustomThreadInterface,
        drop_down: UiDropDownInterface,
        api_control: ApiControlInterface,
        download_manager: DownloadManagerInterface,
        download_video: list[DownloadVideoInterface],
        download_playlist: list[DownloadPlaylistInterface],
        download_essential: DownloadEssentialInterface,
        intent: IntentInterface,
        multi_thread: MultiThreadInterface,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.ids.link.text = intent(platform).get_intent_text()
        self.__message_class = message_class

        # Thread
        self.__multi_thread = multi_thread
        self.__custom_thread = custom_thread
        self.__custom_thread_backup = custom_thread()

        # Drop Down

        self.__drop_down = drop_down()
        self.__drop_down.caller = self.ids.mp4
        self.__drop_down.create_ui(self.set_mp4_text)

        api_control()
        self.__download_manager = download_manager
        self.__download_video = download_video
        self.__download_playlist = download_playlist
        self.__download_essential = download_essential

        # Update

        self.__open_webbrowser = False
        self.__version_url = r"https://raw.githubusercontent.com/JoaoEmanuell/dmyk/master/dmyk/version.py"
        self.verify_update()

    def main(self) -> None:
        try:
            request = Request("https://www.youtube.com")
            urlopen(request, timeout=3)
        except (URLError, timeout):
            self.__message_class.set_out(
                "Sua conexão de internet está indisponível, por favor tente novamente!"
            )
        else:
            try:
                if self.__custom_thread_backup.is_alive():
                    self.__custom_thread_backup.kill()
                    self.__custom_thread_backup.join()
                    self.__message_class.set_out("Download cancelado!")
                    self.__message_class.set_pb(0, 0)
                    self.__message_class.set_ws("download_button", "default")
                    print("Default button main")
                else:
                    self.start_download()
            except (AssertionError, AttributeError):  # Case the thread not created
                self.start_download()

    def start_download(self):
        self.__message_class.set_out("")
        self.__message_class.set_pb(0, 0)

        # Set to None to restart the thread without this case treading error

        self.__custom_thread_backup = None
        self.__custom_thread_backup: CustomThreadInterface = self.__custom_thread()
        try:
            url = str(self.ids.link.text)

            self.__custom_thread_backup.set_thread(
                target=self.__download_manager,
                args=(
                    url,
                    self.verify_mp3(),
                    self.__drop_down.get_text(),
                    self.__download_video,
                    self.__download_playlist,
                    self.__message_class,
                    self.__download_essential,
                ),
            )
            self.__custom_thread_backup.start()

        except Exception as err:
            self.__message_class.set_out(
                f"Alguma coisa deu errado!\nPor favor insira uma nova url\nE tente novamente!\n"
            )
            print(err)

    def verify_mp3(self) -> bool:
        mp3 = self.ids.mp3.state
        mp4 = self.ids.mp4.state
        if mp3 == "down":
            return True
        elif mp4 == "down":
            return False
        else:
            return True

    def show_drop_down(self) -> None:
        self.__drop_down.open()
        self.ids.mp4.state = "down"

    def set_mp4_text(self, *args, **kwargs) -> None:
        self.ids.mp4.text = self.__drop_down.get_text()
        self.ids.mp4.state = "down"

    def mp3_button_selected(self) -> None:
        self.ids.mp4.text = "MP4"

    def verify_update(self) -> None:
        try:
            # Test connection
            request = Request(self.__version_url)
            urlopen(request, timeout=3)
            online_version_file = DownloadContent.download(
                self.__version_url, self.__message_class
            ).decode("utf-8")
            online_version = online_version_file.rsplit("\n")[0]
            if online_version != f'__version__ = "{__version__}"':
                self.__message_class.set_out(
                    'O aplicativo está desatualizado!\nClique aqui ou acesse: \n"https://joaoemanuell.github.io/dmyk/"\nPara obter a versão mais recente!'
                )
                self.__open_webbrowser = True
            self.__message_class.set_pb(0, 0)
        except (URLError, timeout):
            self.__message_class.set_out("Falha na verificação do update!")
        except Exception as err:
            self.__message_class.set_out("Falha na verificação do update!")
            print(f"Update verification error: {err}")

    def output_update(self) -> None:
        if self.__open_webbrowser:
            dmyk_url = r"https://joaoemanuell.github.io/dmyk/"
            if platform == "linux" or platform == "win":
                from webbrowser import open

                open(dmyk_url)
            elif platform == "android":
                from jnius import autoclass

                PythonActivity = autoclass("org.kivy.android.PythonActivity")
                Intent = autoclass("android.content.Intent")
                Uri = autoclass("android.net.Uri")
                intent = Intent(
                    Intent.ACTION_VIEW,
                    Uri.parse(dmyk_url),
                )
                PythonActivity.mActivity.startActivity(intent)


class Main(MDApp):
    def build(self) -> Screen:
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.primary_hue = "500"
        return Tela(
            Message,
            CustomThread,
            UiDropDown,
            ApiControl,
            DownloadManager,
            [YoutubeDlDownloadVideo, PytubeDownloadVideo],
            [YoutubeDLDownloadPlaylist, PytubeDownloadPlaylist],
            download_essential,
            Intent,
            multi_thread,
        )

    def on_start(self):
        service.start_service()

    def on_stop(self):
        service.stop_service()

    def on_pause(self):
        return True

    def on_resume(self):
        pass


if __name__ == "__main__":
    Android()
    Main().run()
