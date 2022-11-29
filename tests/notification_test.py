from sys import path
path.append('..')

from kivy.utils import platform

from source_notification import Notification, notification

def test_answer():
    notification_obj = Notification(platform)

    notification_obj.send_notification(
        title='Test',
        description='Description'
    )

    notification.send_notification(
        title='Test 2',
        description='Description 2'
    )