"""Don't execute with pytest"""

from sys import path
from time import sleep

path.append("../")

from source_thread import CustomThread

thread_value_check = True


def test_answer():
    print("Alert, don't execute with pytest!!!")
    custom_thread = CustomThread()
    custom_thread.set_thread(target=thread_test)
    custom_thread.start()
    print("Started thread")
    sleep(1)
    print("\nKill thread")
    print(custom_thread.is_alive())
    custom_thread.kill()  # Kill the thread
    custom_thread.join()
    print("End thread")
    assert thread_value_check == True
    print("Restart thread!")
    custom_thread = None
    custom_thread = CustomThread()
    custom_thread.set_thread(target=thread_test)
    custom_thread.start()


def thread_test(*args, **kwargs) -> None:
    global thread_value_check
    print(f"Thread value check: {thread_value_check}")
    for i in range(1, 100):
        sleep(0.01)
        print(i, end=", ")
    print("End sleep")
    thread_value_check = False


if __name__ == "__main__":
    test_answer()
