"""
    This module contains the Message class.
"""

from kivy.app import App
from kivy.clock import mainthread

from .interfaces import MessageInterface

class Message(MessageInterface):
    @classmethod
    @mainthread
    def set_output(cls, text: str='') -> None:
        App.get_running_app().root.ids.output.text = str(text)

    @classmethod
    @mainthread
    def set_progressbar(cls, max: int=100, percent: int=0) -> None:
        App.get_running_app().root.ids.progressbar.max = int(max)
        App.get_running_app().root.ids.progressbar.value = int(percent)

    @classmethod
    @mainthread
    def set_download_button_text(cls, text: str='') -> None:
        App.get_running_app().root.ids.download_button.text = str(text)

    @classmethod
    def set_out(cls, text: str='') -> None:
        cls.set_output(text)

    @classmethod    
    def set_pb(cls, max: int=100, percent: int=0) -> None:
        cls.set_progressbar(max, percent)

    @classmethod
    def set_dbt(cls, text: str='') -> None:
        cls.set_download_button_text(text)