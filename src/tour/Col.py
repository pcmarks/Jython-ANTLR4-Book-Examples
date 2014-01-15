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
from org.antlr.v4.runtime import ParserRuleContext
from org.antlr.v4.runtime import Token

import RowsLexer
import RowsParser

import sys

def main():
    ais = ANTLRFileStream(sys.argv[2])
    lexer = RowsLexer(ais)
    tokens = CommonTokenStream(lexer)
    col = int(sys.argv[1])
    parser = RowsParser(tokens, col)	# Pass column number
    parser.setBuildParseTree(False)		# Don't waste time building a tree
    parser.file()						# Parse


if __name__ == '__main__':
    main()


