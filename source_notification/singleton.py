from kivy.utils import platform

from .notification import Notification

notification = Notification(
    platform=platform, 
    icon_path=None
)