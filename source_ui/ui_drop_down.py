from kivy.uix.dropdown import DropDown
from kivy.uix.togglebutton import ToggleButton

class UiDropDown(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__qualities = ('480p', '360p', '240p', '144p')
        self.size_hint_y = None
        self.max_height = 2000
        self.__text = '720p'
        self.__create_ui()

    def __create_ui(self) -> None:
        buttons_group = 'drop_down_quality'
        button_ui_arg = {'size_hint_y': None, 'height': 80}
        btn_720 = ToggleButton(
            text='720p', group=buttons_group, state='down', **button_ui_arg
        )
        btn_720.bind(
                on_release=lambda btn: (
                    self.__set_text(btn.text), self.select('')
                )
            )
        self.add_widget(btn_720)
        for quality in self.__qualities:
            btn = ToggleButton(
                text=quality, group=buttons_group, **button_ui_arg
            )
            btn.bind(
                on_release=lambda btn: (
                    self.__set_text(btn.text), self.select('')
                )
            )
            self.add_widget(btn)

    def get_text(self) -> str:
        return self.__text

    def __set_text(self, text: str='') -> None:
        self.__text = text