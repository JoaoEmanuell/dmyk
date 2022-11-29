from abc import ABC, abstractmethod

class NotificationInterface(ABC):
    """
    Notification is a class to manager notification for dmyk!
    Using 'pynotifier' to linux and windows!
    """
    @abstractmethod
    def __init__(self, platform: str=None, icon_path: str=None) -> None:
        """Init

        Args:
            platform (str): Platform on running project.
            icon_path (str): Icon path, not include extension, or None if not icon.
        """        
        raise NotImplementedError()

    @abstractmethod
    def send_notification(self, title: str='', description: str='', \
        duration: int=5, urgency: str='normal') -> None:
        """Send a notification to user

        Args:
            title (str): Title of notification.
            description (str): Description of notification.
            duration (int): Duration on notification, in seconds.
            urgency (str): Urgency of notification. Defaults to 'normal'.
        """        
        raise NotImplementedError()