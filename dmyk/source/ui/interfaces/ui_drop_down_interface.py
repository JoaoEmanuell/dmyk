from abc import abstractmethod
from typing import Callable, Optional


class UiDropDownInterface:
    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def create_ui(self, release_callback: Optional[Callable] = None) -> None:
        """Create the itens and add to dropdown

        Args:
            release_callback (Optional[Callable], optional): Callback to touch in the dropdown item. Defaults to None.
        """
        raise NotImplementedError()
