import lark

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
#tree = parser.parse("123+4*5")
#tree = parser.parse("(123+4)*5")
#tree = parser.parse("(123+4)*((5+6)/(7+8))+9")

print(f"tree={tree}")
print(tree.pretty())

#@lark.v_args(inline=True)
class Calculate(lark.Transformer):
    def number(self, xs):
        print(f"xs={xs}")
        return int(xs[0].value)

    def add(self, xs):
        return xs[0] + xs[1]

res = Calculate().transform(tree)
print(f"res={res}")

print(res.pretty())


