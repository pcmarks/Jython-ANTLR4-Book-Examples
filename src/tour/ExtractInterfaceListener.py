
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
  
