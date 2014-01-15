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
from org.antlr.v4.runtime.tree import ParseTreeWalker

import sys

import JavaLexer
import JavaParser
from InsertSerialIDListener import InsertSerialIDListener

def main():
    ais = ANTLRFileStream(sys.argv[1])
    lexer = JavaLexer(ais)
    tokens = CommonTokenStream(lexer)
    parser = JavaParser(tokens)
    tree = parser.compilationUnit()
    walker = ParseTreeWalker()
    extractor = InsertSerialIDListener(tokens)
    walker.walk(extractor, tree)
    print extractor.rewriter.getText()

if __name__ == '__main__':
    main()
