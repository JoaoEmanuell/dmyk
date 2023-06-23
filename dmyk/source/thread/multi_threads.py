from random import randint

from .interfaces import MultiThreadInterface, CustomThreadInterface


class MultiThread(MultiThreadInterface):
    def __init__(self) -> None:
        self.__threads: dict[int, CustomThreadInterface] = {}

    def register_thread(self, thread: CustomThreadInterface) -> int:
        thread_number = randint(1, 100000)
        self.__threads[thread_number] = thread
        return thread_number

    def run_thread(self, thread_number: int) -> None:
        try:
            thread = self.__threads[thread_number]
            thread.start()
        except KeyError:
            print(f"Thread: {thread_number} not found!")

    def kill_thread(self, thread_number: int) -> None:
        try:
            thread = self.__threads[thread_number]
            thread.kill()
            thread.join()
            self.__threads.pop(thread_number)
        except KeyError:
            print(f"Thread: {thread_number} not found!")

    def kill_all_threads(self) -> None:
        for k, v in self.__threads.items():
            v.kill()
            self.__threads.pop(k)
