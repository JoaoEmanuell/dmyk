# Global imports

from re import findall

# Local imports

from .interfaces import (
    DownloadEssentialInterface,
    DownloadPlaylistInterface,
    MessageInterface,
    DownloadVideoInterface,
)


class DownloadManager:
    def __init__(
        self,
        link: str,
        mp3: bool,
        quality: str,
        video: DownloadVideoInterface,
        playlist: DownloadPlaylistInterface,
        message: MessageInterface,
        download_essential: DownloadEssentialInterface,
    ) -> None:

        self.__link = str(link)
        self.__mp3 = bool(mp3)
        self.__quality = str(quality)

        self.__video = video
        self.__playlist = playlist
        self.__download_essential = download_essential
        self.__message = message

        self.main()

    def private__verify_url(self) -> bool:
        verify_tuple_regex = (
            r"^(https:\/\/www.youtube.com\/)",  # domain full
            r"^(https:\/\/youtu.be\/)",  # domain short
            r"^(https:\/\/youtube.com\/)",  # other domain [self.__playlist shared]
        )

        for verify in verify_tuple_regex:
            if len(findall(verify, self.__link)) != 0:
                return True  # Verify regex

        return False

    def private__verify_playlist(self) -> bool:
        verify_url = findall(r"(self.__playlist\?list=)", self.__link)
        if len(verify_url) != 0:
            return True
        else:
            return False

    def main(self) -> None:

        print("Iniciando o download")
        try:
            obj_dict = {
                "playlist": [
                    self.__playlist,
                    "playlist",
                    self.__playlist.download_playlist,
                ],
                "vídeo": [self.__video, "vídeo", self.__video.download_video],
                "música": [self.__video, "música", self.__video.download_audio],
            }
            
            if self.private__verify_url():
                self.__download_essential.create_directory("Música")
                if self.private__verify_playlist():
                    print("Verificado playlist, iniciando o download da playlist")
                    self.__playlist(
                        self.__link, self.__mp3, self.__quality
                    ).download_playlist(self.__video)
                else:
                    print("Verificado vídeo!")
                    if self.__mp3:
                        self.set_dbt_style_text("stop")
                        print("Iniciando download da música")
                        self.__video(
                            self.__link, self.__mp3, self.__quality
                        ).download_audio()
                        self.set_dbt_style_text()
                    else:
                        self.set_dbt_style_text("stop")
                        print("Iniciando download do vídeo")
                        self.__video(
                            self.__link, self.__mp3, self.__quality
                        ).download_video()
                        self.set_dbt_style_text()
            else:
                self.__message.set_out("Erro, url invalida!")
                self.set_dbt_style_text()

        except Exception as Ex:
            self.__message.set_out("YouTube quebrou o app:/")
            self.set_dbt_style_text()
            print(f"ERROR:{Ex.with_traceback()}")

    def set_dbt_style_text(self, background_style: str = "default") -> None:
        self.__message.set_dbt("Baixar Música ou self.__playlist")
        self.__message.set_ws("download_button", "background_color", background_style)
