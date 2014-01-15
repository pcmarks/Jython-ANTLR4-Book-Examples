"""
 * Excerpted from "The Definitive ANTLR 4 Reference",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material, 
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose. 
 * Visit http://www.pragmaticprogrammer.com/titles/tpantlr2 for more book information.

 Translated to Python by Peter C Marks

"""

from org.antlr.v4.runtime import ANTLRFileStream
from org.antlr.v4.runtime import CommonTokenStream

import LabeledExprLexer
import LabeledExprParser
from EvalVisitor import EvalVisitor

import sys

def main():
	ais = ANTLRFileStream(sys.argv[1])
	lexer = LabeledExprLexer(ais)
	tokens = CommonTokenStream(lexer)
	parser = LabeledExprParser(tokens);
	tree = parser.prog()

	eval = EvalVisitor()
	eval.visit(tree)

if __name__ == '__main__':
	main()

