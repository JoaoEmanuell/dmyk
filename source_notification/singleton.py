from kivy.utils import platform

from .notification import Notification

notification = Notification(
    platform=platform,
    title='DMYK',
    icon_path=None
)