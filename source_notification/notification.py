from typing import Type

from .interfaces import NotificationInterface, AndroidNotificationInterface

class Notification(NotificationInterface):
    def __init__(self, platform: str = None, title: str='', \
        icon_path: str = None, \
        android_notification: Type[AndroidNotificationInterface]=None) -> None:
        self.__platform = str(platform)
        self.__title = str(title)
        self.__desktop_platforms = ('win', 'linux', )
        self.__android_notification = android_notification
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
            from pynotifier import Notification as PyNotification

            PyNotification(
                title=self.__title,
                description=description,
                duration=duration,
                icon_path=self.__icon_path,
                urgency=urgency
            ).send()

        elif self.__platform == 'android':
            print(f"Start android notification {__file__}")
            self.progress_notification()
            print("Finished android notification")

    def progress_notification(self, max: int=100, actual: int=0, \
        infinity: bool=False) -> None:
        if self.__platform == 'android':
            self.__android_notification.progress_notification(
                max, actual, infinity
            )
            '''from jnius import autoclass
        
            print('Android Notification!')
            mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
            context = mActivity.getApplicationContext()
            SetProgress = autoclass(".ProgressBar")
            print(f'SetProgress : {SetProgress}')
            SetProgress.set_progress(
                mActivity, context, 'test', 'test text', max, actual, infinity
            )'''
