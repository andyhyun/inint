from lexer import *


def main():
    with open("test_programs/10.txt", "r") as program:
        text = program.read()
    lexical_analyzer = Lexer(text)
    print("Lexical analysis is starting:\n")
    token_count = 0
    tok = lexical_analyzer.get_next_token()
    while tok != Token(TokenType.EOF, "", 0):
        print(tok)
        token_count += 1
        tok = lexical_analyzer.get_next_token()
    print(tok)
    print("\nLexical analysis is now complete:")
    print(f"\tNumber of tokens: {token_count + 1}")
    print(f"\tNumber of lines: {lexical_analyzer.line_number}")


if __name__ == "__main__":
    main()
