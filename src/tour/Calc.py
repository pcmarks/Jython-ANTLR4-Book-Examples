from org.antlr.v4.runtime import ANTLRFileStream
from org.antlr.v4.runtime import CommonTokenStream

import LabeledExprLexer
import LabeledExprParser
from EvalVisitor import EvalVisitor

import sys

ais = ANTLRFileStream(sys.argv[1])
lexer = LabeledExprLexer(ais)
tokens = CommonTokenStream(lexer)
parser = LabeledExprParser(tokens);
tree = parser.prog()

eval = EvalVisitor()
eval.visit(tree)

