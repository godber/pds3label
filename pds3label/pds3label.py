import os

try:
    from collections import OrderedDict
except:
    # supporting py 2.6
    from ordereddict import OrderedDict


from .pds3_label_visitor import Pds3LabelVisitor

from antlr4 import FileStream, CommonTokenStream
from .vendor.pds3_python.ODLv21Lexer import ODLv21Lexer
from .vendor.pds3_python.ODLv21Parser import ODLv21Parser


class Pds3Label(OrderedDict):
    """The Pds3Label parses and stores the provided PDS3 label"""

    def __init__(self, infile):
        if not os.path.exists(infile):
            raise
        self.infile = infile
        self._parse_tree = None

        super(Pds3Label, self).__init__(self.parse_label())


    def parse_label(self):
        """Parses the label in self.infile with the ANTLR visitor
           returns the ordered label dictionary used to initialize
           the Pds3Label object's OrderedDict.
        """
        # TODO: make this work with attached labels as well as
        # stand alone labels.
        # Save the RAW full text of the label to self._raw
        input_stream = FileStream(self.infile)
        lexer = ODLv21Lexer(input_stream)
        tokens = CommonTokenStream(lexer)

        parser = ODLv21Parser(tokens)
        parse_tree = parser.label()
        self._parse_tree = parse_tree
        visitor = Pds3LabelVisitor()
        visitor.visit(parse_tree)
        return visitor.root_dict
