
import LabeledExprBaseVisitor
import LabeledExprParser

class EvalVisitor(LabeledExprBaseVisitor):

	def __init__(self):
		self.memory = dict()

	# ID '=' expr NEWLINE
	def visitAssign(self, ctx):
		id = ctx.ID().getText()
		value = self.visit(ctx.expr());
		self.memory[id] = value
		return value

	# expr NEWLINE	
	def visitPrintExpr(self, ctx):
		value = self.visit(ctx.expr())
		print "%d" % value
		return 0

	# INT	
	def visitInt(self, ctx):
		return int(ctx.INT().getText())
		
	# ID
	def visitId(self, ctx):
		id = ctx.ID().getText()
		if id in self.memory:
			return self.memory[id]
		else:
			return 0

	# expr op=('*'|'/') expr
	def visitMulDiv(self, ctx):
		left = self.visit(ctx.expr(0))
		right = self.visit(ctx.expr(1))
		if ctx.op.getType() == LabeledExprParser.MUL: 
			return left * right
		else:
			return left / right

	# expr op=('+'|'/') expr
	def visitAddSub(self, ctx):
		left = self.visit(ctx.expr(0))
		right = self.visit(ctx.expr(1))
		if ctx.op.getType() == LabeledExprParser.ADD: 
			return left + right
		else:
			return left - right
	
	# '(' expr ')'	
	def visitParens(self, ctx):
		return self.visit(ctx.expr())





