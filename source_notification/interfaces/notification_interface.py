from abc import ABC, abstractmethod

class NotificationInterface(ABC):
    """
    Notification is a class to manager notification for dmyk!
    Using 'pynotifier' to linux and windows!
    """
    @abstractmethod
    def __init__(self, platform: str=None, title: str='', icon_path: str=None) -> None:
        """Init

        Args:
            platform (str): Platform on running project.
            title (str): Title of notification.
            icon_path (str): Icon path, not include extension, or None if not icon.
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