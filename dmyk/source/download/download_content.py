from io import BytesIO
from urllib.request import Request, urlopen
from os.path import join

from .interfaces import DownloadContentInterface, MessageInterface


class DownloadContent(DownloadContentInterface):
    @classmethod
    def download(cls, url: str, message: MessageInterface) -> bytes:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

        with urlopen(request) as response:
            file: bytes = b""
            length = response.getheader("content-Length")
            block_size = 1000000  # 1MB Default

            if length:
                length = int(length)
                block_size = max(4096, length // 20)

            print(f"Len: {length} blocksize: {block_size}")

            buffer_all = BytesIO()
            size = 0

            while True:
                buffer_now = response.read(block_size)
                file += buffer_now

                if not buffer_now:
                    break

                buffer_all.write(buffer_now)
                size += len(buffer_now)

                if length:
                    message.set_progressbar(int(length), int(size))

            return file

    @classmethod
    def save_file(cls, name: str = "", dir: str = ".", content: bytes = b"") -> None:
        print(name, dir)
        print(join(dir, name))
        with open(join(dir, name), "wb") as f:
            f.write(content)
