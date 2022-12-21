from abc import abstractmethod


class UiDropDownInterface:
    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError()
