from urllib.request import Request, urlopen
from os import remove, mkdir
from requests import head
from time import sleep

from source.thread import MultiThreadInterface, CustomThreadInterface
from source.utils import MessageInterface
from ..interfaces import MultiPartDownloadInterface
from source.utils import MultiPartDownloadException


class MultiPartDownload(MultiPartDownloadInterface):
    def __init__(
        self,
        part_number: int,
        multi_thread: MultiThreadInterface,
        custom_thread: CustomThreadInterface,
        message: MessageInterface,
        path: str,
    ) -> None:
        self.__part_number = part_number
        self.__multi_thread = multi_thread
        self.__custom_thread = custom_thread
        self.__message = message
        self.__path = f"{path}/Música"
        self.__retry = 0
        self.__parts_path = f"./parts/"
        try:
            mkdir(self.__parts_path)
        except FileExistsError:
            pass

    def download(self, url: str, headers: dict, filename: str) -> None:
        response = head(url, allow_redirects=True)
        file_size = int(response.headers["Content-Length"])

        # Retry

        if file_size == 0:
            print("Retry download!")
            self.__retry += 1
            if self.__retry == 10:
                raise MultiPartDownloadException()
            else:
                self.download(url, headers, filename)

        chunk_size = file_size // self.__part_number

        threads: list[int] = []
        for i in range(self.__part_number):
            start_byte = i * chunk_size
            end_byte = start_byte + chunk_size - 1

            if i == self.__part_number - 1:
                end_byte = file_size - 1

            # Range
            headers["Range"] = f"bytes={start_byte}-{end_byte}"

            # Thread

            thread = self.__custom_thread()

            thread.set_thread(target=self.__download_chunk, args=(url, headers, i + 1))

            thread_id = self.__multi_thread.register_thread(thread)

            self.__multi_thread.run_thread(thread_id)

            threads.append(thread_id)

        # Verify if threads is running

        not_activate_threads = []
        while True:
            for thread_id in threads:
                thread_state = self.__multi_thread.is_alive(thread_id)
                if not thread_state and thread_id not in not_activate_threads:
                    not_activate_threads.append(thread_id)
            if len(not_activate_threads) == len(threads):
                break
            else:
                sleep(1)

        # Remove threads from multi_thread
        for thread_id in not_activate_threads:
            self.__multi_thread.kill_thread(thread_id)

        self.__message.set_out("Unindo as partes, aguarde um pouco!")
        self.__union_parts(f"{self.__path}/{filename}")
        self.__message.set_out("União das partes finalizada!")

    def __download_chunk(self, url: str, headers: dict, chunk_number: int) -> None:
        """Download chunk file

        Args:
            url (str): Url to complete file
            headers (dict): Headers to request, contain the range for download
            chunk_number (int): Number of chunk, to determinate the part.
        """
        request = Request(url, headers=headers)
        filename = f"{self.__parts_path}/{chunk_number}.dat"

        # Create a initial file with empty data

        with open(filename, "w") as part:
            part.write("")

        with urlopen(request) as response:
            file: bytes = b""
            length = response.getheader("content-Length")
            block_size = 1000000  # 1MB Default

            if length:
                length = int(length)
                block_size = max(4096, length // 20)

            # print(f"Len : {length} blocksize : {block_size}")

            size = 0

            while True:
                buffer_now = response.read(block_size)
                file = buffer_now

                if not buffer_now:  # End loop
                    break

                size += len(buffer_now)

                if length:
                    # print(f"Part: {chunk_number} | size: {size} | length: {length}")
                    self.__message.set_pb(max=length, percent=size)
                # Append data on file
                with open(filename, "ab") as part:
                    part.write(file)

    def __union_parts(self, filename: str) -> None:
        """Union all parts in one file

        Args:
            filename (str): Filename to save the file
        """
        # Create a initial file with empty data
        with open(filename, "w") as file:
            file.write("")

        for i in range(self.__part_number):
            part_file_name = f"{self.__parts_path}/{i + 1}.dat"
            # Open part
            with open(part_file_name, "rb") as part:
                # Open complete file
                with open(filename, "ab") as complete:
                    # Append part on complete file
                    complete.write(part.read())
            # Remove part
            remove(part_file_name)
