class Error(Exception):

    def __init__(self, message):
        self.message = f"{self.__class__.__name__}: {message}"


class LexerError(Error):
    pass


class ParserError(Error):
    pass
