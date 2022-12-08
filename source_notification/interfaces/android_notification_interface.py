from abc import ABC, abstractclassmethod

class AndroidNotificationInterface(ABC):
    @abstractclassmethod
    def progress_notification(cls, max: int=100, actual: int=0, \
        infinity: bool=False) -> None:
        """Progress notification
        To remove notification set max and min equals 0

        Args:
            max (int, optional): Max progress. Defaults to 100.
            actual (int, optional): Min progress. Defaults to 0.
            infinity (bool, optional): If true this progress bar is 
                infinity, else no. Default False
        """        
        raise NotImplementedError()