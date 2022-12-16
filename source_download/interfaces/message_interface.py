from abc import ABC, abstractclassmethod

class MessageInterface(ABC):
    """This class send message to interface in main thread."""    
    @abstractclassmethod
    def set_output(text: str='') -> None:
        """Set output text

        Args:
            text (str): Text to set in output.
        """        
        raise NotImplementedError()

    @abstractclassmethod
    def set_progressbar(max: int=100, percent: int=0) -> None:
        """Set progress bar

        Args:
            max (int): Max progress bar. Defaults to 100.
            percent (int): Actual percent on progress bar. Defaults to 0.
        """        
        raise NotImplementedError()

    @abstractclassmethod
    def set_download_button_text(text: str='') -> None:
        """Set the download button text

        Args:
            text (str): New text to button. Defaults to ''.
        """        
        raise NotImplementedError()

    @abstractclassmethod
    def set_out(text: str='') -> None:
        """Set output text alias

        Args:
            text (str): Text to set in output.
        """
        raise NotImplementedError()

    @abstractclassmethod
    def set_pb(max: int=100, percent: int=0) -> None:
        """Set progress bar alias

        Args:
            max (int): Max progress bar. Defaults to 100.
            percent (int): Actual percent on progress bar. Defaults to 0.
        """        
        raise NotImplementedError()

    @abstractclassmethod
    def set_dbt(text: str='') -> None:
        """Set the download button text alias

        Args:
            text (str): New text to button. Defaults to ''.
        """        
        raise NotImplementedError()