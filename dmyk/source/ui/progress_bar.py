from kivymd.uix.progressbar.progressbar import ProgressBar

from .interfaces import ProgressBarInterface


class ProgressBar(ProgressBar, ProgressBarInterface):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        # Style

        self.color = (0.5, 1, 0, 1)

    def set_max_value(self, max: int = 100, value: int = 0) -> None:
        self.max = int(max)
        self.value = int(value)
