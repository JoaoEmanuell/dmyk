from sys import path

path.append("../")

from download import DownloadVerify


def test_answer():
    url = "https://www.youtube.com/watch?v=IKgj0YMWfkE"
    download = DownloadVerify

    # Url verify
    ## Domain full
    data = download.verify_url(url)
    assert data == True

    ## Domain short
    url = "https://youtu.be/IKgj0YMWfkE"
    data = download.verify_url(url)
    assert data == True

    ## No domain
    url = ""
    data = download.verify_url(url)
    assert data == False

    ## Playlist
    url = "https://www.youtube.com/playlist?list= \
        PLucm8g_ezqNrYgjXC8_CgbvHbvI7dDfhs"

    data = download.verify_playlist(url)
    assert data == True

    data = download.verify_playlist("")
    assert data == False
