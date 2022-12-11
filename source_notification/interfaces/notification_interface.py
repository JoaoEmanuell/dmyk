from abc import ABC, abstractmethod
from typing import Type

from .android_notification_interface import AndroidNotificationInterface

class NotificationInterface(ABC):
    """
    Notification is a class to manager notification for dmyk!
    Using 'pynotifier' to linux and windows!
    """
    @abstractmethod
    def __init__(self, platform: str=None, title: str='', icon_path: str=None, \
        android_notification: Type[AndroidNotificationInterface]=None) -> None:
        """Init

        Args:
            platform (str): Platform on running project.
            title (str): Title of notification.
            icon_path (str): Icon path, not include extension, or None if not icon.
            android_notification (AndroidNotificationInterface): Android notification class
        """        
        raise NotImplementedError()

    @abstractmethod
    def send_notification(self, description: str='', \
        duration: int=3, urgency: str='normal') -> None:
        """Send a notification to user

        Args:
            description (str): Description of notification.
            duration (int): Duration on notification, in seconds.
            urgency (str): Urgency of notification. Defaults to 'normal'.
        """        
        raise NotImplementedError()

    @abstractmethod
    def progress_notification(self, max: int=100, actual: int=0, \
        infinity: bool=False) -> None:
        """Progress notification [Exclusive for Android]
        To remove notification set max and min equals 0

        Args:
            max (int, optional): Max progress. Defaults to 100.
            actual (int, optional): Min progress. Defaults to 0.
            infinity (bool, optional): If true this progress bar is 
                infinity, else no. Default False
        """  
        raise NotImplementedError()