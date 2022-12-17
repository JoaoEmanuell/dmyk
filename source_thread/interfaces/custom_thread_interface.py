from abc import ABC, abstractmethod

class CustomThreadInterface(ABC):
    @abstractmethod
    def start(self) -> None:
        """Start thread, use at the place run"""
        raise NotImplementedError()

    @abstractmethod
    def kill(self) -> None:
        """Kill the thread, allows the use of join without erros""" 
        raise NotImplementedError()

    @abstractmethod
    def set_thread(self, *args, **keywords) -> None:
        """Same thread args, use to set thread""" 
        raise NotImplementedError()