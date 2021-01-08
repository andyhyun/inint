from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
import sys


def main():
    arg_num = len(sys.argv) - 1
    if arg_num < 1:
        raise Exception("No file found")
    if arg_num > 1:
        raise Exception("Only 1 file allowed")
    with open(sys.argv[1], "r") as file:
        text = file.read()
    lexer = Lexer(text)
    token_list = lexer.get_token_list()
    parser = Parser(token_list)
    ast = parser.program()
    interpreter = Interpreter(ast)
    interpreter.interpret()


if __name__ == "__main__":
    main()
