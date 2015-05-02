import os

from .pds3_label_visitor import Pds3LabelVisitor

from antlr4 import FileStream, CommonTokenStream
from .vendor.pds3_python.ODLv21Lexer import ODLv21Lexer
from .vendor.pds3_python.ODLv21Parser import ODLv21Parser


class Pds3Label(object):
    """The Pds3Label parses and stores the provided PDS3 label"""

    def __init__(self, infile):
        if not os.path.exists(infile):
            raise
        self.infile = infile
        self._parse_tree = None
        self._visitor = None

        self.parse_label()

    def parse_label(self):
        input_stream = FileStream(self.infile)
        lexer = ODLv21Lexer(input_stream)
        tokens = CommonTokenStream(lexer)

        parser = ODLv21Parser(tokens)
        parse_tree = parser.label()
        self._parse_tree = parse_tree
        visitor = Pds3LabelVisitor()
        visitor.visit(parse_tree)
