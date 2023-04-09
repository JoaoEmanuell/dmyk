from abc import abstractmethod


class ProgressBarInterface:
    """Progress bar interface"""

    @abstractmethod
    def set_max_value(self, max: int = 100, value: int = 0) -> None:
        """Set the progress bar values

        Args:
            max (int, optional): Max value from bar. Defaults to 100.
            value (int, optional): Value from bar. Defaults to 0.

        """
        raise NotImplementedError()
