from .download import DownloadEssential, DownloadContent, Message
from .api import ApiControl
from .ui import UiDropDown

download_essential = DownloadEssential(ApiControl(), DownloadContent, Message)
ui_drop_down_obj = UiDropDown()
