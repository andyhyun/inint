class Token:

    def __init__(self, token_type, value, line_number):
        self.token_type = token_type
        self.value = value
        self.line_number = line_number

    def __str__(self):
        """String representation of a Token"""
        return f"{self.token_type} ({self.value}) on Line {self.line_number}"

    def __repr__(self):
        return self.__str__()
