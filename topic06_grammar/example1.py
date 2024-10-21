import lark

# This is the grammar for valid arithmetic expressions.
grammar = r"""
    start: sum

    sum: product
        | sum "+" product
        | sum "-" product

    product: atom
        | product "*" atom
        | product "/" atom

    atom: NUMBER
        | "(" sum ")"

    # "Terminals" are written in all uppercase.
    # They cannot have production rules.
    NUMBER: /-?[0-9]+/

"""
parser = lark.Lark(grammar)

tree = parser.parse("123")
tree = parser.parse("123+4")
tree = parser.parse("123+4*5")
#tree = parser.parse("(123+4)*5")
#tree = parser.parse("(123+4)*((5+6)/(7+8))+9")

# The function parser.parse() creates a *parse tree*
# from the input string.
# Technically, a parse tree is slightly more general than an
# *abstract syntax tree* (AST).
# But if you see someone refer to an AST,
# you should think about the output of parser.parse.

# The parse tree can be visualized by either:
#print(f"tree={tree}")
#print(f"tree.pretty()={tree.pretty()}")
#lark.tree.pydot__tree_to_png(tree, "test.png")
