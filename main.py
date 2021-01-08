from token_type import TokenType
from lexer import Lexer
from parse import Parser
from interpreter import Interpreter


def main():
    with open("test_programs/11.txt", "r") as program:
        text = program.read()
    lexical_analyzer = Lexer(text)
    print("Lexical analysis is starting:\n")
    token_count = 0
    tok = lexical_analyzer.get_next_token()
    while tok.token_type != TokenType.EOF:
        print(tok)
        token_count += 1
        tok = lexical_analyzer.get_next_token()
    print(tok)
    print("\nLexical analysis is now complete:")
    print(f"\tNumber of tokens: {token_count + 1}")
    print(f"\tNumber of lines: {lexical_analyzer.line_number}\n\n")

    parse_test_lexer = Lexer(text)
    token_list = parse_test_lexer.get_token_list()
    parser = Parser(token_list)
    print("Parsing has started:\n")
    prog = parser.program()
    print("\nSuccessful parse")

    interpreter_test_parser = Parser(token_list)
    tree = interpreter_test_parser.program()
    interpret = Interpreter(tree)
    interpret.interpret()


if __name__ == "__main__":
    main()
