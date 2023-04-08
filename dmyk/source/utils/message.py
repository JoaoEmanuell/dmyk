"""This module contains the Message class."""

from typing import Any

from kivy.app import App
from kivy.clock import mainthread
from kivymd.uix.progressbar.progressbar import ProgressBar
from kivymd.uix.boxlayout import BoxLayout

from ..styles import styles as style_dict
from .interfaces import MessageInterface


class Message(MessageInterface):
    progress_bar = ProgressBar()
    progress_bar.background_color = (0.27, 0.79, 0.93, 0.9)
    progress_bar.color = (0.5, 1, 0, 1)

    @classmethod
    @mainthread
    def set_output(cls, text: str = "") -> None:
        App.get_running_app().root.ids.output.text = str(text)

    @classmethod
    @mainthread
    def set_progressbar(cls, max: int = 100, percent: int = 0) -> None:
        main_box = App.get_running_app().root.ids.box
        main_box.remove_widget(cls.progress_bar)
        cls.progress_bar.max = max
        cls.progress_bar.value = percent
        main_box.add_widget(cls.progress_bar)
        if max == 100 and percent == 100 or max == 0 and percent == 0:
            main_box.remove_widget(cls.progress_bar)

    @classmethod
    @mainthread
    def set_download_button_text(cls, text: str = "") -> None:
        App.get_running_app().root.ids.download_button.text = str(text)

    @classmethod
    @mainthread
    def set_widget_style(cls, widget_id: str = "", style: str = "") -> None:

        styles: dict[str, Any] = style_dict[widget_id][style]
        for key, value in styles.items():
            setattr(
                getattr(App.get_running_app().root.ids, widget_id),  # Get widget
                key,
                value,
            )  # Set style on widget

    # Alias

    @classmethod
    def set_out(cls, text: str = "") -> None:
        cls.set_output(text)

    @classmethod
    def set_pb(cls, max: int = 100, percent: int = 0) -> None:
        cls.set_progressbar(max, percent)

    @classmethod
    def set_dbt(cls, text: str = "") -> None:
        cls.set_download_button_text(text)

    @classmethod
    def set_ws(cls, widget_id: str = "", style: str = "") -> None:

        cls.set_widget_style(widget_id, style)
