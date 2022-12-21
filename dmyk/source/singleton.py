from .download import DownloadEssential, DownloadContent, Message
from .api import ApiControl

download_essential = DownloadEssential(ApiControl(), DownloadContent, Message)
