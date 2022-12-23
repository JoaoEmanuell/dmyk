from abc import ABC, abstractmethod


class IntentInterface(ABC):
    """Intent is a class to get intent on android."""

    @abstractmethod
    def __init__(self, platform: str) -> None:
        """Init

        Args:
            platform (str): platform on running app
        """
        raise NotImplementedError()

    @abstractmethod
    def get_intent_text(self) -> str:
        """Get intent text

        Returns:
            str: Intent text
        """
        raise NotImplementedError()
