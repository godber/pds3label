# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by ODLv21Parser.

class ODLv21Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by ODLv21Parser#label.
    def visitLabel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#assignment_stmt.
    def visitAssignment_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#pointer_stmt.
    def visitPointer_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#object_stmt.
    def visitObject_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#group_stmt.
    def visitGroup_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#value.
    def visitValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#date_time_value.
    def visitDate_time_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#sequence_value.
    def visitSequence_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#sequence_1D.
    def visitSequence_1D(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#sequence_2D.
    def visitSequence_2D(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#set_value.
    def visitSet_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#ScalarInteger.
    def visitScalarInteger(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#ScalarBasedInteger.
    def visitScalarBasedInteger(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#ScalarFloat.
    def visitScalarFloat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#ScalarScaledReal.
    def visitScalarScaledReal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#ScalarIdentifier.
    def visitScalarIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#ScalarSymbol.
    def visitScalarSymbol(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#ScalarString.
    def visitScalarString(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#units_expression.
    def visitUnits_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#units_factor.
    def visitUnits_factor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ODLv21Parser#namespace_identifier.
    def visitNamespace_identifier(self, ctx):
        return self.visitChildren(ctx)


