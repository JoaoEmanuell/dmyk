from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

from .interfaces import BoxLayoutProgressBarInterface, ProgressBarInterface


class BoxLayoutProgressBar(BoxLayout, BoxLayoutProgressBarInterface):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        # Style

        self.padding = [0, 55, 0, 55]

        with self.canvas.before:
            Color(0.27, 0.79, 0.99, 0.9)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def set_progressbar(self, progress_bar: ProgressBarInterface) -> None:
        self.add_widget(progress_bar)
