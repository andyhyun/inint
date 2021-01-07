from enum import Enum, auto
from token_type import TokenType
from token_class import Token
import error

KEYWORDS = {
    "print": TokenType.PRINT,
    "begin": TokenType.BEGIN,
    "end": TokenType.END,
    "if": TokenType.IF,
    "then": TokenType.THEN,
}


class State(Enum):
    START = auto()
    IN_IDENT = auto()
    IN_ICONST = auto()
    IN_RCONST = auto()
    IN_SCONST = auto()
    IN_COMMENT = auto()
    POSSIBLE_RCONST = auto()
    POSSIBLE_COMMENT = auto()


class Lexer:

    def __init__(self, text):
        self.text = text
        self.char_position = 0
        self.current_char = self.text[self.char_position]
        self.current_lexeme = ""
        self.line_number = 1
        self.current_state = State.START

    def error(self, message=""):
        if len(message) == 0:
            raise error.ININTLexerError(f"'{self.current_lexeme}' on line {self.line_number}")
        raise error.ININTLexerError(message)

    def advance(self):
        self.char_position += 1
        if self.char_position >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.char_position]

    def token_to_be_returned(self):
        lexeme = self.current_lexeme
        return_token = None
        if len(self.current_lexeme) == 0:
            return_token = Token(TokenType.EOF, TokenType.EOF.value, self.line_number)
        elif self.current_state == State.IN_IDENT:
            if lexeme in KEYWORDS:
                return_token = Token(KEYWORDS[lexeme], lexeme, self.line_number)
            else:
                return_token = Token(TokenType.IDENT, lexeme, self.line_number)
        elif self.current_state == State.IN_ICONST:
            return_token = Token(TokenType.ICONST, int(lexeme), self.line_number)
        elif self.current_state == State.IN_RCONST:
            return_token = Token(TokenType.RCONST, float(lexeme), self.line_number)
        elif self.current_state == State.IN_SCONST:
            return_token = Token(TokenType.SCONST, lexeme, self.line_number)
        else:
            self.error()
        self.current_state = State.START
        self.current_lexeme = ""
        return return_token

    def get_token_list(self):
        token_list = []
        tok = self.get_next_token()
        while tok.token_type != TokenType.EOF:
            token_list.append(tok)
            tok = self.get_next_token()
        token_list.append(tok)
        return token_list

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_state == State.START:
                if self.current_char == "\n":
                    self.line_number += 1
                elif self.current_char.isspace():
                    self.advance()
                    continue
                elif self.current_char == "\"":
                    self.current_state = State.IN_SCONST
                elif self.current_char == "/":
                    self.current_state = State.POSSIBLE_COMMENT
                elif self.current_char.isalpha():
                    self.current_lexeme += self.current_char
                    self.current_state = State.IN_IDENT
                elif self.current_char.isdigit():
                    self.current_lexeme += self.current_char
                    self.current_state = State.IN_ICONST
                elif self.current_char == ".":
                    self.current_lexeme += self.current_char
                    self.current_state = State.POSSIBLE_RCONST
                elif self.current_char in "+-*/=();":
                    returned_token_type = TokenType(self.current_char)
                    returned_char = self.current_char
                    self.advance()
                    return Token(returned_token_type, returned_char, self.line_number)
                else:
                    self.current_lexeme += self.current_char
                    self.error()
                self.advance()
                continue
            elif self.current_state == State.IN_IDENT:
                if self.current_char.isalnum():
                    self.current_lexeme += self.current_char
                    self.advance()
                else:
                    return self.token_to_be_returned()
            elif self.current_state == State.IN_ICONST:
                if self.current_char == ".":
                    self.current_lexeme += self.current_char
                    self.current_state = State.POSSIBLE_RCONST
                    self.advance()
                elif self.current_char.isdigit():
                    self.current_lexeme += self.current_char
                    self.advance()
                else:
                    return self.token_to_be_returned()
            elif self.current_state == State.POSSIBLE_RCONST:
                if self.current_char.isdigit():
                    self.current_lexeme += self.current_char
                    self.current_state = State.IN_RCONST
                    self.advance()
                else:
                    self.current_lexeme += self.current_char
                    self.error()
            elif self.current_state == State.IN_RCONST:
                if self.current_char.isdigit():
                    self.current_lexeme += self.current_char
                    self.advance()
                else:
                    return self.token_to_be_returned()
            elif self.current_state == State.IN_SCONST:
                if self.current_char == "\n":
                    self.error(f"Strings must be on one line at line {self.line_number}")
                elif self.current_char == "\"":
                    self.advance()
                    return self.token_to_be_returned()
                else:
                    self.current_lexeme += self.current_char
                    self.advance()
            elif self.current_state == State.POSSIBLE_COMMENT:
                if self.current_char == "/":
                    self.current_state = State.IN_COMMENT
                    self.advance()
                else:
                    self.current_state = State.START
                    return Token(TokenType.DIV, "/", self.line_number)
            elif self.current_state == State.IN_COMMENT:
                if self.current_char == "\n":
                    self.current_state = State.START
                else:
                    self.advance()
        return self.token_to_be_returned()
