from .download_content import DownloadContent
from .download_essential import DownloadEssential
from .download_manager import DownloadManager

# Pytube

from .download_pytube import PytubeDownloadPlaylist, PytubeDownloadVideo

# YoutubeDL

from .download_youtube_dl import YoutubeDlDownloadVideo, YoutubeDLDownloadPlaylist

# Interfaces

from .interfaces import (
    DownloadVideoInterface,
    DownloadContentInterface,
    DownloadManagerInterface,
    DownloadEssentialInterface,
    DownloadPlaylistInterface,
)
