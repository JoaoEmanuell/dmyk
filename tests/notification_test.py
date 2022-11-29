from sys import path
path.append('..')

from kivy.utils import platform

from source_notification import Notification, notification

def test_answer():
    notification_obj = Notification(platform, 'Test')

    notification_obj.send_notification(
        description='Description'
    )

    notification_obj = Notification('test', 'Test 2')
    
    notification_obj.send_notification('Description 2') # Not send

    notification.send_notification(
        description='Description 3'
    )