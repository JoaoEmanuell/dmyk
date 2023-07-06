from random import randint

from .interfaces import MultiThreadInterface, CustomThreadInterface


class MultiThread(MultiThreadInterface):
    def __init__(self) -> None:
        self.__threads: dict[int, CustomThreadInterface] = {}
        self.__kill_threads_retry = 0

    def register_thread(self, thread: CustomThreadInterface) -> int:
        thread_number = randint(1, 100000)
        self.__threads[thread_number] = thread
        return thread_number

    def run_thread(self, thread_number: int) -> None:
        try:
            thread = self.__threads[thread_number]
            thread.start()
        except KeyError:
            self.__thread_not_found(thread_number)

    def kill_thread(self, thread_number: int) -> None:
        try:
            thread = self.__threads[thread_number]
            thread.kill()
            thread.join()
            self.__threads.pop(thread_number)
        except KeyError:
            self.__thread_not_found(thread_number)

    def kill_all_threads(self) -> None:
        try:
            for k, v in self.__threads.items():
                v.kill()
                self.__threads.pop(k)
            self.__kill_threads_retry = 0
        except RuntimeError:
            print(f"RuntimeError to kill threads {self.__kill_threads_retry}")
            if self.__kill_threads_retry != 100:
                self.__kill_threads_retry += 1
                self.kill_all_threads()
            else:
                raise Exception(f"Error to kill threads! {self.__kill_threads_retry}")

    def is_alive(self, thread_number: int) -> bool:
        try:
            thread = self.__threads[thread_number]
            return thread.is_alive()
        except KeyError:
            self.__thread_not_found(thread_number)

    def __thread_not_found(self, thread_number: int) -> None:
        print(f"Thread: {thread_number} not found!")
