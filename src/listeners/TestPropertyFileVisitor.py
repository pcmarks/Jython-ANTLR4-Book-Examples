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

import PropertyFileBaseVisitor
import PropertyFileLexer
import PropertyFileParser


class PropertyFileVisitor(PropertyFileBaseVisitor):

	def __init__(self):
		self.props = dict()

	def visitProp(self, ctx):
		id = ctx.ID().getText()		# prop : ID '=' STRING '\n' ;
		value = ctx.STRING().getText()
		self.props[id] = value
		return None

def main():
    ais = ANTLRFileStream(sys.argv[1])
    lexer = PropertyFileLexer(ais)
    tokens = CommonTokenStream(lexer)
    parser = PropertyFileParser(tokens)
    tree = parser.file()

    loader = PropertyFileVisitor()
    loader.visit(tree)

    print loader.props

if __name__ == '__main__':
    main()
    
