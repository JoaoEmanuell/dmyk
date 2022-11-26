from abc import ABC, abstractclassmethod

class MessageInterface(ABC):
    """This class send message to interface in main thread."""    
    @abstractclassmethod
    def set_output(text: str=''):
        """Set output text

        Args:
            text (str): Text to set in output.
        """        
        raise NotImplementedError()

    @abstractclassmethod
    def set_progressbar(max: int=100, percent: int=0):
        """Set progress bar

        Args:
            max (int): Max progress bar. Defaults to 100.
            percent (int): Actual percent on progress bar. Defaults to 0.
        """        
        raise NotImplementedError()