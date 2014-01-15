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
from org.antlr.v4.runtime.misc import MultiMap
from org.antlr.v4.runtime.tree import ParseTreeWalker

import CymbolLexer
import CymbolParser
import CymbolBaseListener

class Graph():
	
	def __init__(self):
		self.nodes = []
		self.edges = MultiMap()

	def edge(self, source, target):
		self.edges.map(source, target)

	def toString(self):
		return "edges: %s, functions: %s" % (self.edges.toString(), self.nodes)

	def toDOT(self):
		buf = ''.join(["digraph G{\n", "  ranksep=.25;\n", "  edge [arrowsize=.5]\n",
						"  node [shape=circle, fontname=\"ArialNarrow\",\n",
						"        fontsize=12, fixedsize=true, height=.45];\n", "  "])
		for src in self.edges.keySet():
			for trg in self.edges.get(src):
				buf = ''.join([buf, "  ", src, " -> ", trg, ";\n"])
		buf = buf + "}\n"
		return buf

class FunctionListener(CymbolBaseListener):

	def __init__(self):
		self.graph = Graph()
		self.currentFunctionName = None

	def enterFunctionDecl(self, ctx):
		self.currentFunctionName = ctx.ID().getText()
		self.graph.nodes.append(self.currentFunctionName)

	def exitCall(self, ctx):
		funcName = ctx.ID().getText()
		self.graph.edge(self.currentFunctionName, funcName)

def main():
	ais = ANTLRFileStream(sys.argv[1])
	lexer = CymbolLexer(ais)
	tokens = CommonTokenStream(lexer)
	parser = CymbolParser(tokens)
	parser.setBuildParseTree(True)
	tree = parser.file()

	#print tree.toStringTree(parser)

	walker = ParseTreeWalker()
	collector = FunctionListener()
	walker.walk(collector, tree)
	#print collector.graph.toString()
	print collector.graph.toDOT()


if __name__ == '__main__':
	main()

