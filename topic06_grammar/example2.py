import lark

# Lark implements several "nonstandard" features on top of BNF.
# 1) ? before the rule name
#    Removes the rule from the parse tree if it has only one child
# 2) -> after a |
#    Renames the node in the parse tree,
#    so that you can determine which choice was made
# 3) The %import / %ignore lines ignore whitespace
grammar = r"""
    start: sum

    ?sum: product
        | sum "+" product   -> add
        | sum "-" product   -> mul

    ?product: atom
        | product "*" atom  -> mul
        | product "/" atom  -> div

    ?atom: NUMBER
        | "(" sum ")"

    NUMBER: /-?[0-9]+/

    %import common.WS_INLINE
    %ignore WS_INLINE
"""
parser = lark.Lark(grammar)

tree = parser.parse("123")
tree = parser.parse("123+4")
tree = parser.parse("123+4*5")
#tree = parser.parse("(123+4)*5")
#tree = parser.parse("(123+4)*((5+6)/(7+8))+9")

