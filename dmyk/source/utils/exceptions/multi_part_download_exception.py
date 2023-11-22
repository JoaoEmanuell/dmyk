class MultiPartDownloadException(Exception):
    """Multi part download exception class"""
    def __init__(self, message: str="Multi part download error") -> None:
        self.message = message
        super().__init__(self.message)

