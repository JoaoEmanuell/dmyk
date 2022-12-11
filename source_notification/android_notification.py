from .interfaces import AndroidNotificationInterface

class AndroidNotification(AndroidNotificationInterface):
    @classmethod
    def progress_notification(cls, max: int=100, actual: int=0, \
        infinity: bool=False) -> None:
        
        '''from pathlib import Path
        from jnius_config import set_classpath, get_classpath
        path = str(Path().absolute()) + '/*'
        print(path)
        set_classpath('.', path)
        print(get_classpath())
        from jnius import autoclass
        
        print('Android Notification!')
        mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
        context = mActivity.getApplicationContext()
        path_to_progress = str(Path().absolute()).replace('/data', '')[1::].replace('/', '.')
        print(path_to_progress)
        SetProgress = autoclass(f"{path_to_progress}.ProgressBar")
        print(f'SetProgress : {SetProgress}')
        SetProgress.set_progress(
            mActivity, context, 'test', 'test text', max, actual, infinity
        )'''
        '''from jnius import autoclass
        AndroidNotification = autoclass('android.app.NotificationManager')
        print(AndroidNotification)
        NotificationCompact = autoclass('android.support.v4.app.NotificationCompat')
        print(NotificationCompact)'''
        from jnius import autoclass
        autoclass('org.jnius.NativeInvocationHandler')
        import plyer
        plyer.notification.notify(title='Test', message='Notification using plyer')
