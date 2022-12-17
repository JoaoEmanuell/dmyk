from abc import ABC, abstractmethod

class ServiceInterface(ABC):
    """Android app service manager"""
    @abstractmethod
    def __init__(self, platform: str='') -> None:
        """
        Args:
            platform (str, optional): platform on running app
        """        
        raise NotImplementedError()
    
    @abstractmethod
    def start_service(self) -> bool:
        """Start app service"""        
        raise NotImplementedError()
    
    @abstractmethod
    def stop_service(self) -> bool:
        """Stop app service"""
        raise NotImplementedError()