from abc import abstractmethod
from .progress_bar_interface import ProgressBarInterface


class BoxLayoutProgressBarInterface:
    @abstractmethod
    def set_progressbar(self, progress_bar: ProgressBarInterface) -> None:
        """Set the progressbar on Box Layout

        Args:
            progress_bar (ProgressBarInterface): Progress bar widget
        """
        raise NotImplementedError()
