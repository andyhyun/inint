from enum import Enum

"""All of the token types that are to be used by the Token object"""


class TokenType(Enum):
    PRINT   = "print"
    BEGIN   = "begin"
    END     = "end"
    IF      = "if"
    IDENT   = "IDENT"
    ICONST  = "ICONST"
    RCONST  = "RCONST"
    SCONST  = "SCONST"
    PLUS    = "+"
    MINUS   = "="
    MULT    = "*"
    DIV     = "/"
    EQ      = "="
    LPAREN  = "("
    RPAREN  = ")"
    COLON   = ":"
    SCOLON  = ";"
