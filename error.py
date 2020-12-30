class Error(Exception):

    def __init__(self, message: str):
        self.message = f"{self.__class__.__name__}: {message}"


class LexerError(Error):
    pass