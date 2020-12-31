from token_type import TokenType


class Token:

    def __init__(self, type, value, line_number):
        self.type = type
        self.value = value
        self.line_number = line_number

    def __eq__(self, other):
        return self.type == other.type

    def __ne__(self, other):
        return self.type != other.type

    def __str__(self):
        """String representation of a Token"""
        return f"{self.type} ({self.value}) on Line {self.line_number}"

    def __repr__(self):
        return self.__str__()
