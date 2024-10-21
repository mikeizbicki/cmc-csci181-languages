import re
import lark

# A *language* is a subset of valid strings.


# Regular languages are defined by regular expressions.
# A standard example is the language of `ab` repeated 
# an arbitrary number of times.
regex = r'^(ab)+$'
pattern = re.compile(regex)
pattern.match("ab")         # in language
pattern.match("abab")       # in language
pattern.match("abababab")   # in language
pattern.match("ac")         # not in language
pattern.match("ba")         # not in language
pattern.match("baba")       # not in language


# Languages can more generally be represented by a *grammar*.
# A grammar is a set of *production rules* which define a procedure
# for *generating* strings in the language.
# Some synonyms for grammar include: 
# - "Backus-Naur Form" (BNF)
# - "Extended Backus-Naur Form" (EBNF)
# The language above (called `(ab)+`) can be defined
# by the following grammar.
grammar = r'''
start: "ab" | "ab" start
'''
parser = lark.Lark(grammar)
parser.parse("ab")         # in language
parser.parse("abab")       # in language
parser.parse("abababab")   # in language
parser.parse("abc")        # not in language
parser.parse("ba")         # not in language
parser.parse("baba")       # not in language


# Grammars can be used to represent languages that are not regular.
# The following language is called $a^nb^n$.
# It is not regular, but *context free*.
grammar = r'''
start: "ab" | "a" start "b"
'''
parser = lark.Lark(grammar)
parser.parse("ab")          # in language
parser.parse("aabb")        # in language
parser.parse("aaaabbbb")    # in language
parser.parse("aaaabbb")     # not in language
parser.parse("aaaacbbbb")   # not in language


# The language of balanced parenthesis is the prototypical example
# of a context free language that is not regular.
# It is also called the "dyck language".
grammar = r'''
start: "()" | "(" start+ ")"
'''
parser = lark.Lark(grammar)
parser.parse("()")          # in language
parser.parse("(()())")      # in language
parser.parse("(()(())())")  # in language
parser.parse("(()")         # not in language
parser.parse("())")         # not in language


# The dyck-2 language is the language of balanced parenthesis
# with two types of parenthesis.
grammar = r'''
start: "()" | "(" start+ ")"
     | "[]" | "[" start+ "]"
'''
parser = lark.Lark(grammar)
parser.parse("()")          # in language
parser.parse("([]())")      # in language
parser.parse("[[]()]")      # in language
parser.parse("[[]([])()]")  # in language
parser.parse("(]")          # not in language
parser.parse("[(])")        # not in language
