from __future__ import print_function
import re

try:
    from collections import OrderedDict
except:
    # supporting py 2.6
    from ordereddict import OrderedDict

from .vendor.pds3_python.ODLv21Visitor import ODLv21Visitor


class Pds3LabelVisitor(ODLv21Visitor):
    """Walks the ANTLR Parse tree and generates label data structure"""

    def __init__(self):
        super(Pds3LabelVisitor, self).__init__()
        # root_dict is the top level dictionary
        self.root_dict = OrderedDict()
        # current_dict is used to keep track of the nesting level for
        # assignments.
        self.current_dict = self.root_dict

    def visitAssignment_stmt(self, ctx):
        val = self.visitChildren(ctx)
        print("%s = %s" % (ctx.IDENTIFIER().getText(), val))
        self.current_dict[ctx.IDENTIFIER().getText()] = val
        return val

    def visitValue(self, ctx):
        return ODLv21Visitor.visitChildren(self, ctx)

    def visitScalarFloat(self, ctx):
        ODLv21Visitor.visitScalarFloat(self, ctx)
        return float(ctx.FLOAT().getText())

    def visitScalarInteger(self, ctx):
        ODLv21Visitor.visitScalarInteger(self, ctx)
        return int(ctx.INTEGER().getText())

    def visitScalarIdentifier(self, ctx):
        ODLv21Visitor.visitScalarIdentifier(self, ctx)
        return ctx.IDENTIFIER().getText()

    def visitScalarString(self, ctx):
        ODLv21Visitor.visitScalarString(self, ctx)
        return Pds3LabelVisitor._clean_string(ctx.STRING().getText())

    def visitScalarSymbol(self, ctx):
        ODLv21Visitor.visitScalarSymbol(self, ctx)
        return Pds3LabelVisitor._clean_symbol(ctx.SYMBOL_STRING().getText())

    def visitObject_stmt(self, ctx):
        object_identifier = Pds3LabelVisitor._get_object_identifier(ctx)
        object_dict = OrderedDict([('_type', 'OBJECT')])
        self.current_dict[object_identifier] = object_dict
        self.current_dict = object_dict

        w = self.visitChildren(ctx)

        # TODO: I think the line below implicitly assumes single nesting
        self.current_dict = self.root_dict
        return w

    def visitGroup_stmt(self, ctx):
        group_identifier = Pds3LabelVisitor._get_object_identifier(ctx)
        group_dict = OrderedDict([('_type', 'GROUP')])
        self.current_dict[group_identifier] = group_dict
        self.current_dict = group_dict

        w = self.visitChildren(ctx)

        self.current_dict = self.root_dict
        return w

    @classmethod
    def _get_object_identifier(cls, ctx):
        """This method handles the unanticipated list returned by the
        object.IDENTIFIER().  It will return the text from a SINGLE
        identifier
        """
        identifiers = []
        for identifier in ctx.IDENTIFIER():
            identifiers.append(identifier.getText())

        if len(set(identifiers)) != 1:
            print("WARNING Object Identifiers Don't Match")
            print(set(identifiers))

        return identifiers[0]

    @classmethod
    def _clean_symbol(cls, instring):
        """Strips the single quotes off of the symbol"""
        instring = re.sub(r"'", '', instring)
        return instring

    @classmethod
    def _clean_string(cls, instring):
        """Cleans up the provided string, including the following things:
            * Strips off double quotes
            * Replaces all whitespace (including newlines) with a single space.
        """
        instring = re.sub(r'"', '', instring)          # strip "
        instring = re.sub(r"-\s*\n\s+", '', instring)  # remove hyphen and its trailing whitespace
        instring = re.sub(r"\s+", ' ', instring)       # replace whitespace with single space
        return instring
