from pynotifier import Notification as PyNotification

from .interfaces import NotificationInterface

class Notification(NotificationInterface):
    def __init__(self, platform: str = None, icon_path: str = None) -> None:
        self.__platform = str(platform)

        # Validate icon path
        if self.__platform == 'linux' and icon_path != None:
            self.__icon_path = f'{icon_path}.png'
        elif self.__platform == 'windows' and icon_path != None:
            self.__icon_path = f'{icon_path}.ico'
        else:
            self.__icon_path = None

    def send_notification(self, title: str = '', description: str = '', \
        duration: int = 5, urgency: str = 'normal') -> None:

        if self.__platform == 'windows' or self.__platform == 'linux':

            PyNotification(
                title=title,
                description=description,
                duration=duration,
                icon_path=self.__icon_path,
                urgency=urgency
            ).send()