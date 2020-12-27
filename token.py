class Token:

    def __init__(self, type, value, line_number):
        self.type = type
        self.value = value
        self.line_number = line_number

    def __str__(self):
        """String representation of a Token"""
        return f"Token Info:\n\tType: {self.type}\n\tValue: {self.value}\n\tLine: {self.line_number}\n"

    def __repr__(self):
        return self.__str__()
