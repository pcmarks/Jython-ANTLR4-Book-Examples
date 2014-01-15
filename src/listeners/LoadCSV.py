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

import CSVLexer
import CSVParser
import CSVBaseListener

class Loader(CSVBaseListener):

    def __init__(self):
        self.EMPTY = ""
        self.rows = [dict()]
        self.header = []
        self.currentRowFieldValues = None

    def exitHdr(self, ctx):
        self.header = []
        self.header.extend(self.currentRowFieldValues)

    def enterRow(self, ctx):
        self.currentRowFieldValues = []

    def exitRow(self, ctx):
        if ctx.getParent().getRuleIndex() == CSVParser.RULE_hdr:
            return None
        m = dict()
        i = 0
        for v in self.currentRowFieldValues:
            m[self.header[i]] = v
            i = i + 1
        self.rows.append(m)

    def exitString(self, ctx):
        self.currentRowFieldValues.append(ctx.STRING().getText())

    def exitText(self, ctx):
        self.currentRowFieldValues.append(ctx.TEXT().getText())

    def exitEmpty(self, ctx):
        self.currentRowFieldValues.append(self.EMPTY)

def main():
    ais = ANTLRFileStream(sys.argv[1])
    lexer = CSVLexer(ais)
    tokens = CommonTokenStream(lexer)
    parser = CSVParser(tokens)
    parser.setBuildParseTree(True)
    tree = parser.file()

    print tree.toStringTree(parser)

    walker = ParseTreeWalker()
    loader = Loader()
    walker.walk(loader, tree)
    for row in loader.rows:
	    print row

if __name__ == '__main__':
    main()

