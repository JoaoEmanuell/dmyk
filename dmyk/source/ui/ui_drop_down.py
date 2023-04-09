from typing import Callable, Optional

from kivy.metrics import dp
from kivymd.uix.menu.menu import MDDropdownMenu
from kivymd.color_definitions import colors

from .interfaces import UiDropDownInterface


class UiDropDown(MDDropdownMenu, UiDropDownInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__qualities = ("720p", "480p", "360p", "240p", "144p")
        self.size_hint_y = None
        self.max_height = dp(300)
        self.__text = "720p"
        self.width_mult = 1.25
        self.background_color = colors['Blue']['700']
        self.border_margin = dp(4)
        self.position = 'center'
        

    def create_ui(self, release_callback: Optional[Callable] = None) -> None:
        items = []
        for quality in self.__qualities:
            button = {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"{quality}",
                "divider": 'Full',
                "divider_color": (1, 1, 1, 1),
                "divider_height": 1,
                "on_release": lambda x=f"{quality}": (
                    self.__set_text(x),
                    release_callback(text=quality) if release_callback else None,
                    self.dismiss(),
                ),
            }
            items.append(button)
        self.items = items

    def get_text(self) -> str:
        return self.__text

    def __set_text(self, text: str = "") -> None:
        self.__text = text
