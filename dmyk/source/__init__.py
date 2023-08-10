# Android import

from .android import (
    Android,
    Service,
    service,
    Intent,
    ServiceInterface,
    IntentInterface,
)

# Api control

from .api import ApiControl, ApiControlInterface

# Download

from .download import (
    DownloadContent,
    DownloadEssential,
    PytubeDownloadPlaylist,
    PytubeDownloadVideo,
    DownloadManager,
    DownloadPlaylistInterface,
    DownloadContentInterface,
    DownloadEssentialInterface,
    DownloadManagerInterface,
    DownloadVideoInterface,
    YoutubeDlDownloadVideo,
    YoutubeDLDownloadPlaylist,
    MultiPartDownload,
    MultiPartDownloadInterface,
    DownloadRemotePlaylistYoutubeDl,
    DownloadRemoteVideoYoutubeDl
)

# Custom thread

from .thread import (
    CustomThread,
    CustomThreadInterface,
    MultiThread,
    MultiThreadInterface,
)

# Ui

from .ui import UiDropDown, UiDropDownInterface

# Styles

from .styles import styles

# Singleton

from .singleton import download_essential, multi_thread

# Utils

from .utils import Message, MessageInterface
