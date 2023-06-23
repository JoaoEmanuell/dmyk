from abc import ABC, abstractmethod

from .custom_thread_interface import CustomThreadInterface


class MultiThreadInterface(ABC):
    """Multi thread manager class"""

    def __init__(self) -> None:
        """Init"""
        raise NotImplementedError()

    def register_thread(self, thread: CustomThreadInterface) -> int:
        """Register the thread

        Args:
            thread (CustomThreadInterface): Custom Thread created

        Returns:
            int: number of thread
        """
        raise NotImplementedError()

    def run_thread(self, thread_number: int) -> None:
        """Run the thread

        Args:
            thread_number (int): Number of thread provide by register
        """
        raise NotImplementedError()

    def kill_thread(self, thread_number: int) -> None:
        """Kill the thread

        Args:
            thread_number (int): Number of thread provide by register
        """
        raise NotImplementedError()

    def kill_all_threads(self) -> None:
        """Kill all threads registered"""
        raise NotImplementedError()
