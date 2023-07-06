from urllib.request import Request, urlopen
from os import remove
from requests import head

from source.thread import MultiThreadInterface, CustomThreadInterface
from source.utils import MessageInterface
from ..interfaces import MultiPartDownloadInterface


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
        self.__path = path
        self.__retry = 0

    def download(self, url: str, headers: dict, filename: str) -> None:
        response = head(url)
        file_size = int(response.headers["Content-Length"])

        # Retry

        if file_size == 0:
            print("Retry download!")
            self.__retry += 1
            if self.__retry == 3:
                raise Exception("Error to download!")
            else:
                self.download(url, headers, filename)

        chunk_size = file_size // self.__part_number

        threads = []
        for i in range(num_chunks):
            start_byte = i * chunk_size
            end_byte = start_byte + chunk_size - 1

            if i == num_chunks - 1:
                end_byte = file_size - 1

            # Range
            headers["Range"] = f"bytes={start_byte}-{end_byte}"

            # Thread

            thread = self.__custom_thread()

            thread = thread.set_thread(
                target=self.__download_chunk, args=(self, url, headers, i + 1)
            )

            thread_id = self.__multi_thread.register_thread(thread)

            self.__multi_thread.run_thread(thread_id)

            threads.append(thread_id)

        for thread in threads:
            self.__multi_thread.kill_thread(thread)

        print("Download complete.")
        print("Union parts")
        self.__union_parts(f"{self.__path}/{filename}")

    def __download_chunk(self, url: str, headers: dict, chunk_number: int) -> None:
        request = Request(url, headers=headers)
        filename = f"{self.__path}/{chunk_number}.dat"

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

            print(f"Len : {length} blocksize : {block_size}")

            size = 0

            while True:
                buffer_now = response.read(block_size)
                file = buffer_now

                if not buffer_now:  # End loop
                    break

                size += len(buffer_now)

                if length:
                    # print(f"Part: {chunk_number} | size: {size} | length: {length}")
                    print(f"Part: {chunk_number} | size: {size} | length: {length}")
                    self.__message.set_pb(
                        max=length, percent=size, part_number=chunk_number
                    )
                # Append data on file
                with open(filename, "ab") as part:
                    part.write(file)

    def __union_parts(self, filename: str) -> None:
        # Create a initial file with empty data
        with open(filename, "w") as file:
            file.write("")

        for i in range(num_chunks):
            print(f"union: part{i + 1}.dat | {i + 1}")
            part_file_name = f"{self.__path}/{i + 1}.dat"
            with open(part_file_name, "rb") as part:
                with open(filename, "ab") as complete:
                    complete.write(part.read())
            remove(part_file_name)
