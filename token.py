from token_type import TokenType

class Token:

    def __init__(self, type: TokenType, value, line_number: int):
        self.type = type
        self.value = value
        self.line_number = line_number

    def __str__(self):
        """String representation of a Token"""
        return f"{self.type} ({self.value}) on Line {self.line_number}"

    def __repr__(self):
        return self.__str__()
