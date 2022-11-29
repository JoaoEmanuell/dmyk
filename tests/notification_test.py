from sys import path
path.append('..')

from kivy.utils import platform

from source_notification import Notification

def test_answer():
    notification = Notification(platform)

    notification.send_notification(
        title='Test',
        description='Description'
    )