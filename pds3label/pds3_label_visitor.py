from .vendor.pds3_python.ODLv21Visitor import ODLv21Visitor


class Pds3LabelVisitor(ODLv21Visitor):
    """Walks the ANTLR Parse tree and generates label data structure"""

    def __init__(self):
        super(Pds3LabelVisitor, self).__init__()

    def visitAssignment_stmt(self, ctx):
        val = self.visitChildren(ctx)
        print "%s = %s" % (ctx.IDENTIFIER().getText(), val)
        return val

    def visitValue(self, ctx):
        return ODLv21Visitor.visitChildren(self, ctx)

    def visitScalarFloat(self, ctx):
        ODLv21Visitor.visitScalarFloat(self, ctx)
        return float(ctx.FLOAT().getText())

    def visitScalarInteger(self, ctx):
        ODLv21Visitor.visitScalarInteger(self, ctx)
        return int(ctx.INTEGER().getText())

    def visitScalarString(self, ctx):
        ODLv21Visitor.visitScalarString(self, ctx)
        return ctx.STRING().getText()

    def visitScalarSymbol(self, ctx):
        ODLv21Visitor.visitScalarSymbol(self, ctx)
        return ctx.SYMBOL_STRING().getText()
