from enum import Enum


class TokenType(Enum):
    """All of the token types that are to be used by the Token object"""

    PRINT = "print"
    BEGIN = "begin"
    END = "end"
    IF = "if"
    THEN = "then"
    IDENT = "IDENT"
    ICONST = "ICONST"
    RCONST = "RCONST"
    SCONST = "SCONST"
    PLUS = "+"
    MINUS = "-"
    MULT = "*"
    DIV = "/"
    EQ = "="
    LPAREN = "("
    RPAREN = ")"
    SCOLON = ";"
    EOF = "EOF"
