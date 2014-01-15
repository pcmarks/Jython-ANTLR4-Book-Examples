"""
 * Excerpted from "The Definitive ANTLR 4 Reference",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material, 
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose. 
 * Visit http://www.pragmaticprogrammer.com/titles/tpantlr2 for more book information.

 Translated to Python by Peter C Marks

"""

from org.antlr.v4.runtime import TokenStream
from org.antlr.v4.runtime import TokenStreamRewriter

import JavaBaseListener

class InsertSerialIDListener(JavaBaseListener):

	def __init__(self, tokens):
		self.rewriter = TokenStreamRewriter(tokens)

	def enterClassBody(self, ctx):
		field = "\n\tpublic static final long serialVersionUID = 1L;"
		self.rewriter.insertAfter(ctx.start, field)


