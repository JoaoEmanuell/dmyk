from threading import Thread
from typing import Dict

from requests import get, post

from .interfaces import ApiControlInterface


class ApiControl(ApiControlInterface):
    def __init__(self) -> None:
        self.__endpoint = "https://mp3-api.fly.dev/api/"
        self.__timeout = 60  # 60 seconds
        self.private__start_api()

    def private__start_api(self) -> None:
        Thread(target=get, args=(self.__endpoint,)).start()

    def upload(self, file_path: str) -> Dict[str, str]:
        with open(file_path, "rb") as file:
            response = post(
                f"{self.__endpoint}upload/",
                files={"file": file},
                timeout=self.__timeout,
            )
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Error:{response.status_code}")

    def get_status(self, hash: str) -> Dict[str, str]:
        response = get(f"{self.__endpoint}status/{hash}", timeout=self.__timeout)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error:{response.status_code}")

    def get_file(self, hash: str) -> Dict[str, str]:
        response = get(f"{self.__endpoint}converteds/{hash}", timeout=self.__timeout)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error:{response.status_code}")

    def delete_file(self, hash: str) -> None:
        get(f"{self.__endpoint}delete/{hash}", timeout=self.__timeout)
