class Error(Exception):

    def __init__(self, message):
        self.message = f"{self.__class__.__name__}: {message}"


class ININTLexerError(Error):
    pass


class ININTParserError(Error):
    pass


class ININTRuntimeError(Error):
    pass
