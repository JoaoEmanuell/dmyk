from .download import DownloadEssential, DownloadContent, MultiPartDownload
from .api import ApiControl
from .ui import UiDropDown
from .utils import Message
from .thread import MultiThread, CustomThread


multi_thread = MultiThread()

multi_part_download = MultiPartDownload(
    part_number=20,
    multi_thread=multi_thread,
    custom_thread=CustomThread,
    message=Message,
    path=DownloadEssential._get_download_path(),
)

download_essential = DownloadEssential(
    ApiControl(), DownloadContent, multi_part_download, Message
)
