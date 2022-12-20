from sys import path
from getpass import getuser
path.append('..')

from kivy.utils import platform
from dmyk.source import DownloadEssential, DownloadContent, DownloadEssentialInterface, ApiControl
from dmyk.source.download.pytube import Stream

def test_answer() -> None:
    download_essential = DownloadEssential(
        api_control=ApiControl(),
        download_content=DownloadContent,
        message=None
    )
    assert isinstance(download_essential, DownloadEssentialInterface)

    # Verify If File Not Exists
    assert download_essential.verify_if_file_not_exists(True, Stream, '')
    assert download_essential.verify_if_file_not_exists(False, Stream, '')

    # Get download path

    path_to_save = download_essential._get_download_path()
    platforms_path = {
        "win": r"C:\Users\%s\Desktop\\" % getuser(),
        "linux": "/home/%s" % getuser(),
    }
    assert path_to_save == platforms_path[platform]
    