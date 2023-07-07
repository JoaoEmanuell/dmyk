from sys import path
from pathlib import Path
from os.path import join, exists
from os import mkdir

path.append("..")

from pytube import YouTube, Playlist


def test_answer() -> None:
    # Vars
    path_to_save = join(Path().absolute(), "source", "download", "test_pytube", "")
    print(path_to_save)

    if not exists(path_to_save):
        mkdir(path_to_save)

    # Download Vídeo

    url_video = r"https://www.youtube.com/watch?v=IKgj0YMWfkE"
    youtube = YouTube(url_video)
    print("Download Vídeo")
    youtube.streams.get_lowest_resolution().download(path_to_save)
    print("Downloaded Audio")
    youtube.streams.get_audio_only().download(path_to_save)

    # Download playlist

    playlist_url = (
        r"https://youtube.com/playlist?list=PLYHoqTjX7zMqNKwL28GuWd8AfVTjF5iB0"
    )
    playlist = Playlist(playlist_url)
    print("Download playlist")
    YouTube(playlist[0]).streams.get_audio_only().download(path_to_save)
