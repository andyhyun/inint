from token_type import TokenType
import error
import ast_class as ast


class Parser:

    def __init__(self, token_list):
        self.token_list = token_list
        self.tok_position = 0
        self.current_token = self.token_list[self.tok_position]

    def error(self, message=""):
        if len(message) == 0:
            raise error.ININTParserError(f"Unexpected {self.current_token.value} on line {self.current_token.line_number}")
        raise error.ININTParserError(message)

    def advance(self):
        self.tok_position += 1
        if self.tok_position >= len(self.token_list):
            self.current_token = None
        else:
            self.current_token = self.token_list[self.tok_position]

    def previous(self):
        return self.token_list[self.tok_position - 1]

    def check(self, tok_type):
        if self.current_token is None:
            return False
        return self.current_token.token_type == tok_type

    def match(self, *tok_types):
        for tok_type in tok_types:
            if self.check(tok_type):
                self.advance()
                return True
        return False

    def consume(self, tok_type, message=""):
        if self.check(tok_type):
            self.advance()
        else:
            self.error(message)

    def program(self):
        self.consume(TokenType.BEGIN, "Expected 'begin' at the beginning of the program")
        program_node = ast.Program(self.stmt_list())
        self.consume(TokenType.END, "Expected 'end' at the end of the program")
        self.consume(TokenType.EOF, f"Unexpected {self.current_token.value} "
                                    f"after 'end' (Line {self.current_token.line_number})")
        return program_node

    def stmt_list(self):
        stmt_list_node = self.stmt()
        is_end = False
        if stmt_list_node == -1:
            self.error("There are no statements in the program")
        while self.match(TokenType.SCOLON):
            right = self.stmt()
            if right == -1:
                is_end = True
                break
            stmt_list_node = ast.Chain(stmt_list_node, right)
        if is_end:
            return stmt_list_node
        self.error(f"Expected ';' after statement (Line {self.current_token.line_number})")

    def stmt(self):
        if self.check(TokenType.PRINT):
            self.advance()
            return self.print_stmt()
        elif self.check(TokenType.IDENT):
            self.advance()
            return self.assign_stmt()
        elif self.check(TokenType.IF):
            self.advance()
            return self.if_stmt()
        elif self.check(TokenType.END):
            return -1
        elif self.check(TokenType.EOF):
            self.error("Expected 'end' at the end of the program")
        self.error(f"Invalid statement at line {self.current_token.line_number}")

    def print_stmt(self):
        self.consume(TokenType.LPAREN, f"Expected '(' after 'print' (Line {self.current_token.line_number})")
        expression = self.expr()
        self.consume(TokenType.RPAREN, f"Expected ')' after the expression (Line {self.current_token.line_number})")
        return ast.Print(expression)

    def assign_stmt(self):
        var = self.previous().value
        self.consume(TokenType.EQ, f"Expected '=' after the variable name (Line {self.current_token.line_number})")
        expression = self.expr()
        return ast.Assign(var, expression)

    def if_stmt(self):
        self.consume(TokenType.LPAREN, f"Expected '(' after 'if' (Line {self.current_token.line_number})")
        condition = self.expr()
        self.consume(TokenType.RPAREN, f"Expected ')' after the expression (Line {self.current_token.line_number})")
        self.consume(TokenType.THEN, f"Expected 'then' after ')' (Line {self.current_token.line_number})")
        then_branch = self.stmt()
        return ast.If(condition, then_branch)

    def expr(self):
        expr_node = self.term()
        while self.match(TokenType.PLUS, TokenType.MINUS):
            operator = self.previous()
            right = self.term()
            expr_node = ast.Binary(expr_node, operator, right)
        return expr_node

    def term(self):
        term_node = self.factor()
        while self.match(TokenType.MULT, TokenType.DIV):
            operator = self.previous()
            right = self.factor()
            term_node = ast.Binary(term_node, operator, right)
        return term_node

    def factor(self):
        if self.check(TokenType.IDENT):
            self.advance()
            return ast.Var(self.previous().value)
        elif self.match(TokenType.ICONST, TokenType.RCONST, TokenType.SCONST):
            return ast.Literal(self.previous().value)
        elif self.check(TokenType.LPAREN):
            self.advance()
            expression = self.expr()
            self.consume(TokenType.RPAREN, f"Expected ')' after the expression (Line {self.current_token.line_number})")
            return ast.Grouping(expression)
        else:
            self.error(f"Invalid character sequence (Line {self.current_token.line_number})")
