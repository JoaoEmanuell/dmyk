from kivy.utils import platform

from .notification import Notification
from .android_notification import AndroidNotification

notification = Notification(
    platform=platform,
    title='DMYK',
    icon_path=None,
    android_notification=AndroidNotification
)