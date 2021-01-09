# ININT
ININT is a minimal programming language, with an interpreter written in Python.

# Grammar
The grammar rules for ININT are (roughly):
```
program     ::= begin stmt_list end
stmt_list   ::= stmt; {stmt;}
stmt        ::= print_stmt | assign_stmt | if_stmt
print_stmt  ::= print(expr)
if_stmt     ::= if(expr) then stmt
assign_stmt ::= var = expr
var         ::= ident
expr        ::= term {(+|-) term}
term        ::= factor {(*|/} factor}
factor      ::= ident | iconst | rconst | sconst | (expr)
```

# Examples
A program calculating the area of a circle with radius *r*:
```
begin
    pi = 3.14159;
    r = 4;
    a1 = pi * r * r;
    r = r * 2;
    a2 = pi * r * r;
    print("Area 1: " + a1);
    print("\nArea 2: " + a2);
end
```

Output:
```
Area 1: 50.26544
Area 2: 201.06176
```

# How to Run
NOTE: The interpreter has only been tested with Python 3.8.4 (makes use of f-strings)

```
python inint.py <path_to_inint_script>
```
