from pynotifier import Notification as PyNotification

from .interfaces import NotificationInterface

class Notification(NotificationInterface):
    def __init__(self, platform: str = None, title: str='', \
        icon_path: str = None) -> None:
        self.__platform = str(platform)
        self.__title = str(title)
        self.__desktop_platforms = ('win', 'linux', )
        platforms_icon = {'linux': 'png', 'win': 'ico'}

        # Validate icon path
        if icon_path == None:
            self.__icon_path = None
        else:
            if self.__platform in self.__desktop_platforms:
                self.__icon_path = platforms_icon[self.__platform]
            else:
                self.__icon_path = None

    def send_notification(self, description: str = '', \
        duration: int = 3, urgency: str = 'normal') -> None:

        if self.__platform in self.__desktop_platforms:

            PyNotification(
                title=self.__title,
                description=description,
                duration=duration,
                icon_path=self.__icon_path,
                urgency=urgency
            ).send()