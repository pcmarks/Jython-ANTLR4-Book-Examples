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
from org.antlr.v4.runtime.tree import ParseTreeProperty

import JSONLexer
import JSONParser
import JSONBaseListener

class XMLEmitter(JSONBaseListener):

    def __init__(self):
        self.xml = ParseTreeProperty()

    def getXML(self, ctx):
        return self.xml.get(ctx)

    def setXML(self, ctx, s):
    #		print "setXML(", ctx,",", s, ")"
        self.xml.put(ctx, s)

    def exitJson(self, ctx):
        self.setXML(ctx, self.getXML(ctx.getChild(0)))

    def exitAnObject(self, ctx):
        buf = "\n"
        for pctx in ctx.pair():
            buf = ''.join(self.getXML(pctx))
        self.setXML(ctx, buf)

    def exitEmptyObject(self, ctx):
        self.setXML(ctx, "")

    def exitArrayOfValues(self, ctx):
        buf = "\n"
        for vctx in ctx.value():
            buf = ''.join(["<element>", self.getXML(vctx), "</element>", "\n"])
        self.setXML(ctx, buf)

    def exitEmptyArray(self, ctx):
        self.setXML(ctx, "")

    def exitPair(self, ctx):
        tag = self.stripQuotes(ctx.STRING().getText())
        vctx = ctx.value()
        x = "<%s>%s</%s>\n" % (tag, self.getXML(vctx), tag)
        self.setXML(ctx, x)

    def exitObjectValue(self, ctx):
        self.setXML(ctx, self.getXML(ctx.object()))

    def exitArrayValue(self, ctx):
        self.setXML(ctx, self.getXML(ctx.array()))

    def exitAtom(self, ctx):
        self.setXML(ctx, ctx.getText())

    def exitString(self, ctx):
        self.setXML(ctx, self.stripQuotes(ctx.getText()))

    def stripQuotes(self, s):
        if s == None or s[0] != '"':
            return s
        return s[1:-1]	

def main():
    ais = ANTLRFileStream(sys.argv[1])
    lexer = JSONLexer(ais)
    tokens = CommonTokenStream(lexer)
    parser = JSONParser(tokens)
    parser.setBuildParseTree(True)
    tree = parser.json()
    print tree
    #print tree.toStringTree(parser)

    walker = ParseTreeWalker()
    converter = XMLEmitter()
    walker.walk(converter, tree)
    print tree
    #print converter.getXML(tree)

if __name__ == '__main__':
    main()

