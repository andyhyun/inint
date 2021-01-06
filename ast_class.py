class AST:
    pass


class Binary(AST):

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class Program(AST):

    def __init__(self, chain):
        # I might do something with program name later
        # self.name = name
        self.chain = chain


class Chain(AST):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Print(AST):

    def __init__(self, expression):
        self.expression = expression


class If(AST):

    def __init__(self, condition, then_branch):
        self.condition = condition
        self.then_branch = then_branch


class Assign(AST):

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Grouping(AST):

    def __init__(self, expression):
        self.expression = expression


class Literal(AST):

    def __init__(self, value):
        self.value = value


class Var(AST):

    def __init__(self, name):
        self.name = name
