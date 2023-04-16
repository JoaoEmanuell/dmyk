"""This module contains the Message class."""

from typing import Any

from kivy.app import App
from kivy.clock import mainthread
from kivy.metrics import dp
from kivymd.color_definitions import colors
from kivymd.uix.spinner.spinner import MDSpinner
from kivymd.uix.progressbar.progressbar import MDProgressBar

from ..styles import styles as style_dict
from .interfaces import MessageInterface


class Message(MessageInterface):
    progress_bar_widget = None
    spinner_widget = None

    @classmethod
    @mainthread
    def set_output(cls, text: str = "") -> None:
        App.get_running_app().root.ids.output.text = str(text)

    @classmethod
    @mainthread
    def set_progressbar(
        cls, max: int = 100, percent: int = 0, bar_type: str = "determinate"
    ) -> None:
        main_box = App.get_running_app().root.ids.box

        print(f"Max: {max} | Percent: {percent} | bar_type : {bar_type}")

        cls.pb_remove_spinner_bar(main_box)

        if bar_type == "indeterminate":
            print("Indeterminate")
            cls.spinner_widget = MDSpinner(
                size_hint=(None, None),
                size=[dp(46), dp(46)],
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                active=True,
                line_width=dp(5),
                palette=[
                    [0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1],
                    [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1],
                    [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1],
                    [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1],
                ],
            )

            cls.pb_remove_spinner_bar(main_box)

            main_box.add_widget(cls.spinner_widget)
        else:
            cls.pb_remove_spinner_bar(main_box)

            cls.progress_bar_widget = MDProgressBar(
                color=(0.5, 1, 0, 1),
                width=main_box.width,
                height=dp(8),
                max=max,
                value=percent,
            )
            main_box.add_widget(cls.progress_bar_widget)
        if max == percent:
            cls.pb_remove_spinner_bar(main_box)

    @classmethod
    def pb_remove_spinner_bar(cls, main_box: any) -> None:
        # Remove spinner and progress bar from main box
        if cls.spinner_widget != None:
            main_box.remove_widget(cls.spinner_widget)
        if cls.progress_bar_widget != None:
            main_box.remove_widget(cls.progress_bar_widget)

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
    def set_pb(
        cls, max: int = 100, percent: int = 0, bar_type: str = "determinate"
    ) -> None:
        cls.set_progressbar(max, percent, bar_type)

    @classmethod
    def set_dbt(cls, text: str = "") -> None:
        cls.set_download_button_text(text)

    @classmethod
    def set_ws(cls, widget_id: str = "", style: str = "") -> None:

        cls.set_widget_style(widget_id, style)
