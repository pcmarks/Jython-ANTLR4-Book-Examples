"""
 * Excerpted from "The Definitive ANTLR 4 Reference",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material, 
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose. 
 * Visit http://www.pragmaticprogrammer.com/titles/tpantlr2 for more book information.

 Translated to Python by Peter C Marks

"""

import sys

from org.antlr.v4.runtime import ANTLRFileStream
from org.antlr.v4.runtime import CommonTokenStream
from org.antlr.v4.runtime.tree import ParseTreeWalker

import ExprLexer
import ExprParser
import ExprBaseListener

class Evaluator(ExprBaseListener):

	def __init__(self):
		self.stack = []

	def exitE(self, ctx):
		if ctx.getChildCount() == 3:
			right = self.stack.pop()
			left = self.stack.pop()
			if ctx.op.getType() == ExprParser.MULT:
				self.stack.append(left * right)
			else:
				self.stack.append(left + right)

	def visitTerminal(self, node):
		symbol = node.getSymbol()
		if symbol.getType() == ExprParser.INT:
			self.stack.append(int(symbol.getText()))

class EvaluatorWithProps(ExprBaseListener):

	def __init__(self):
		self.values = ParseTreeProperty()

	def exitS(self, ctx):
		self.values[ctx] = values[ctx.getChild(0)]

	def exitE(self, ctx):
		if ctx.getChildCount() == 3:
			left = self.values[ctx.e(0)]
			right = self.values[ctx.e(1)]
			if ctx.op.getType() == ExprParser.MULT:
				self.values[ctx] = left * right
			else:
				self.values[ctx] = left + right
		else:
			self.values[ctx] = self.values[ctx.getChild(0)]

	def visitTerminal(self, node):
		symbol = node.getSymbol()
		if symbol.getType() == ExprParser.INT:
			self.values[ctx] = self.values[ctx.getChild(0)]

def main():
	ais = ANTLRFileStream(sys.argv[1])
	lexer = ExprLexer(ais)
	tokens = CommonTokenStream(lexer)
	parser = ExprParser(tokens)
	parser.setBuildParseTree(True)
	tree = parser.s()

	print tree.toStringTree(parser)

	walker = ParseTreeWalker()

	evaluator = Evaluator()
	walker.walk(evaluator, tree)

if __name__ == '__main__':
	main()

