from token_type import TokenType
import error
import ast_class as ast


class Interpreter:

    def __init__(self, tree):
        self.tree = tree
        self.symbol_table = {}

    def error(self, message):
        raise error.ININTRuntimeError(message)

    def is_sconst(self, node):
        if isinstance(node, int) or isinstance(node, float):
            return False
        elif isinstance(node, str):
            return True
        else:
            self.error("Invalid type")

    def perform_operation(self, left, operator, right):
        if (self.is_sconst(left) or self.is_sconst(right)) and operator.token_type != TokenType.PLUS:
            self.error("Cannot perform non-addition operations on strings")
        if operator.token_type == TokenType.PLUS:
            if self.is_sconst(left) or self.is_sconst(right):
                return str(left) + str(right)
            return left + right
        elif operator.token_type == TokenType.MINUS:
            return left - right
        elif operator.token_type == TokenType.MULT:
            return left * right
        elif operator.token_type == TokenType.DIV:
            if right == 0:
                self.error("Cannot divide by 0")
            if isinstance(left, int) and isinstance(right, int) and left % right == 0:
                return left // right
            return left / right
        else:
            self.error("Invalid operator")

    def interpret(self):
        self.visit_Program(self.tree)

    def visit_Program(self, node):
        if isinstance(node.chain, ast.Chain):
            self.visit_Chain(node.chain)
        else:
            self.visit_Stmt(node.chain)

    def visit_Chain(self, node):
        if isinstance(node.left, ast.Chain):
            self.visit_Chain(node.left)
            self.visit_Stmt(node.right)
        else:
            self.visit_Stmt(node.left)
            self.visit_Stmt(node.right)

    def visit_Stmt(self, node):
        if isinstance(node, ast.Print):
            self.visit_Print(node)
        elif isinstance(node, ast.If):
            self.visit_If(node)
        elif isinstance(node, ast.Assign):
            self.visit_Assign(node)
        else:
            self.error("Invalid statement")

    def visit_Print(self, node):
        expr = self.visit_Expr(node.expression)
        if isinstance(expr, str):
            expr = expr.replace("\\n", "\n")
        print(expr, end="")

    def visit_If(self, node):
        cond = self.visit_Expr(node.condition)
        if isinstance(cond, int) and cond != 0:
            self.visit_Stmt(node.then_branch)

    def visit_Assign(self, node):
        val = self.visit_Expr(node.value)
        self.symbol_table[node.name] = val

    def visit_Expr(self, node):
        if isinstance(node, ast.Binary):
            return self.visit_Binary(node)
        elif isinstance(node, ast.Var):
            return self.visit_Var(node)
        elif isinstance(node, ast.Literal):
            return self.visit_Literal(node)
        elif isinstance(node, ast.Grouping):
            return self.visit_Grouping(node)
        else:
            self.error("Invalid expression")

    def visit_Binary(self, node):
        left_node = self.visit_Expr(node.left)
        right_node = self.visit_Expr(node.right)
        op = node.operator
        return self.perform_operation(left_node, op, right_node)

    def visit_Grouping(self, node):
        expr = self.visit_Expr(node.expression)
        return expr

    def visit_Literal(self, node):
        return node.value

    def visit_Var(self, node):
        if node.name in self.symbol_table:
            return self.symbol_table[node.name]
        else:
            self.error(f"Variable '{node.name}' is not defined")
