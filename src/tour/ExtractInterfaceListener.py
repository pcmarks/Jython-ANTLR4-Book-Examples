"""
 * Excerpted from "The Definitive ANTLR 4 Reference",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material, 
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose. 
 * Visit http://www.pragmaticprogrammer.com/titles/tpantlr2 for more book information.

 Translated to Python by Peter C Marks

"""

import org.antlr.v4.runtime.TokenStream
import org.antlr.v4.runtime.misc.Interval

import JavaBaseListener

class ExtractInterfaceListener(JavaBaseListener):

	def __init__(self, parser):
		self.parser = parser

	def enterClassDeclaration(self, ctx):
		print "interface I%s {" % ctx.Identifier()

	def exitClassDeclaration(self, ctx):
		print "}"

	def enterMethodDeclaration(self, ctx):
		tokens = self.parser.getTokenStream()
		type = "void"
		if ctx.type():
			type = tokens.getText(ctx.type());
		args = tokens.getText(ctx.formalParameters())
		print "\t%s %s%s;" % (type, ctx.Identifier(), args)
  
