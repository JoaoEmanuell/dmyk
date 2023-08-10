from .download_content import DownloadContent
from .download_essential import DownloadEssential
from .download_manager import DownloadManager

# Pytube

from .download_pytube import PytubeDownloadPlaylist, PytubeDownloadVideo

# YoutubeDL

from .download_youtube_dl import YoutubeDlDownloadVideo, YoutubeDLDownloadPlaylist

# Remote download

from .download_remote_youtube_dl import DownloadRemoteVideoYoutubeDl, DownloadRemotePlaylistYoutubeDl

# Multi part download

from .multi_part_download import MultiPartDownload

# Interfaces

from .interfaces import (
    DownloadVideoInterface,
    DownloadContentInterface,
    DownloadManagerInterface,
    DownloadEssentialInterface,
    DownloadPlaylistInterface,
    MultiPartDownloadInterface,
)
