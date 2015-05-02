# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ODLv21Listener import ODLv21Listener
    from .ODLv21Visitor import ODLv21Visitor
else:
    from ODLv21Listener import ODLv21Listener
    from ODLv21Visitor import ODLv21Visitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"&\u00e0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2")
        buf.write(u"\7\2&\n\2\f\2\16\2)\13\2\3\2\3\2\3\3\3\3\5\3/\n\3\3\3")
        buf.write(u"\3\3\3\3\3\3\5\3\65\n\3\3\3\3\3\3\3\3\3\5\3;\n\3\3\3")
        buf.write(u"\3\3\3\3\3\3\5\3A\n\3\3\3\3\3\5\3E\n\3\3\4\3\4\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\4\5\4P\n\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\6\3\6\3\6\3\6\5\6[\n\6\3\6\3\6\3\6\3\6\7\6a\n\6\f\6")
        buf.write(u"\16\6d\13\6\3\6\3\6\3\6\5\6i\n\6\3\7\3\7\3\7\3\7\5\7")
        buf.write(u"o\n\7\3\7\3\7\3\7\3\7\7\7u\n\7\f\7\16\7x\13\7\3\7\3\7")
        buf.write(u"\3\7\5\7}\n\7\3\b\3\b\3\b\3\b\5\b\u0083\n\b\3\t\3\t\3")
        buf.write(u"\n\3\n\5\n\u0089\n\n\3\13\3\13\3\13\3\13\7\13\u008f\n")
        buf.write(u"\13\f\13\16\13\u0092\13\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write(u"\7\f\u009a\n\f\f\f\16\f\u009d\13\f\3\f\3\f\3\r\3\r\3")
        buf.write(u"\r\5\r\u00a4\n\r\3\r\3\r\5\r\u00a8\n\r\3\r\3\r\5\r\u00ac")
        buf.write(u"\n\r\7\r\u00ae\n\r\f\r\16\r\u00b1\13\r\3\r\3\r\3\r\3")
        buf.write(u"\r\5\r\u00b7\n\r\3\16\3\16\5\16\u00bb\n\16\3\16\3\16")
        buf.write(u"\5\16\u00bf\n\16\3\16\3\16\5\16\u00c3\n\16\3\16\3\16")
        buf.write(u"\5\16\u00c7\n\16\3\16\3\16\3\16\5\16\u00cc\n\16\3\17")
        buf.write(u"\3\17\3\17\3\17\7\17\u00d2\n\17\f\17\16\17\u00d5\13\17")
        buf.write(u"\3\17\3\17\3\20\3\20\3\20\5\20\u00dc\n\20\3\21\3\21\3")
        buf.write(u"\21\2\2\22\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \2")
        buf.write(u"\5\3\2\3\4\4\2\26\27\33\33\3\2\22\23\u00fb\2\'\3\2\2")
        buf.write(u"\2\4D\3\2\2\2\6O\3\2\2\2\bQ\3\2\2\2\nV\3\2\2\2\fj\3\2")
        buf.write(u"\2\2\16\u0082\3\2\2\2\20\u0084\3\2\2\2\22\u0088\3\2\2")
        buf.write(u"\2\24\u008a\3\2\2\2\26\u0095\3\2\2\2\30\u00b6\3\2\2\2")
        buf.write(u"\32\u00cb\3\2\2\2\34\u00cd\3\2\2\2\36\u00d8\3\2\2\2 ")
        buf.write(u"\u00dd\3\2\2\2\"&\5\4\3\2#&\7%\2\2$&\7$\2\2%\"\3\2\2")
        buf.write(u"\2%#\3\2\2\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2")
        buf.write(u"\2(*\3\2\2\2)\'\3\2\2\2*+\t\2\2\2+\3\3\2\2\2,.\5\6\4")
        buf.write(u"\2-/\7%\2\2.-\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60\61\7$")
        buf.write(u"\2\2\61E\3\2\2\2\62\64\5\b\5\2\63\65\7%\2\2\64\63\3\2")
        buf.write(u"\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66\67\7$\2\2\67E\3\2")
        buf.write(u"\2\28:\5\n\6\29;\7%\2\2:9\3\2\2\2:;\3\2\2\2;<\3\2\2\2")
        buf.write(u"<=\7$\2\2=E\3\2\2\2>@\5\f\7\2?A\7%\2\2@?\3\2\2\2@A\3")
        buf.write(u"\2\2\2AB\3\2\2\2BC\7$\2\2CE\3\2\2\2D,\3\2\2\2D\62\3\2")
        buf.write(u"\2\2D8\3\2\2\2D>\3\2\2\2E\5\3\2\2\2FG\7\35\2\2GH\7\5")
        buf.write(u"\2\2HP\5\16\b\2IJ\5 \21\2JK\7\6\2\2KL\7\35\2\2LM\7\5")
        buf.write(u"\2\2MN\5\16\b\2NP\3\2\2\2OF\3\2\2\2OI\3\2\2\2P\7\3\2")
        buf.write(u"\2\2QR\7\7\2\2RS\7\35\2\2ST\7\5\2\2TU\5\16\b\2U\t\3\2")
        buf.write(u"\2\2VW\7\b\2\2WX\7\5\2\2XZ\7\35\2\2Y[\7%\2\2ZY\3\2\2")
        buf.write(u"\2Z[\3\2\2\2[\\\3\2\2\2\\b\7$\2\2]a\5\4\3\2^a\7%\2\2")
        buf.write(u"_a\7$\2\2`]\3\2\2\2`^\3\2\2\2`_\3\2\2\2ad\3\2\2\2b`\3")
        buf.write(u"\2\2\2bc\3\2\2\2ce\3\2\2\2db\3\2\2\2eh\7\t\2\2fg\7\5")
        buf.write(u"\2\2gi\7\35\2\2hf\3\2\2\2hi\3\2\2\2i\13\3\2\2\2jk\7\n")
        buf.write(u"\2\2kl\7\5\2\2ln\7\35\2\2mo\7%\2\2nm\3\2\2\2no\3\2\2")
        buf.write(u"\2op\3\2\2\2pv\7$\2\2qu\5\4\3\2ru\7%\2\2su\7$\2\2tq\3")
        buf.write(u"\2\2\2tr\3\2\2\2ts\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2")
        buf.write(u"\2\2wy\3\2\2\2xv\3\2\2\2y|\7\13\2\2z{\7\5\2\2{}\7\35")
        buf.write(u"\2\2|z\3\2\2\2|}\3\2\2\2}\r\3\2\2\2~\u0083\5\32\16\2")
        buf.write(u"\177\u0083\5\22\n\2\u0080\u0083\5\30\r\2\u0081\u0083")
        buf.write(u"\5\20\t\2\u0082~\3\2\2\2\u0082\177\3\2\2\2\u0082\u0080")
        buf.write(u"\3\2\2\2\u0082\u0081\3\2\2\2\u0083\17\3\2\2\2\u0084\u0085")
        buf.write(u"\t\3\2\2\u0085\21\3\2\2\2\u0086\u0089\5\24\13\2\u0087")
        buf.write(u"\u0089\5\26\f\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2")
        buf.write(u"\2\u0089\23\3\2\2\2\u008a\u008b\7\f\2\2\u008b\u0090\5")
        buf.write(u"\32\16\2\u008c\u008d\7\r\2\2\u008d\u008f\5\32\16\2\u008e")
        buf.write(u"\u008c\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2")
        buf.write(u"\2\u0090\u0091\3\2\2\2\u0091\u0093\3\2\2\2\u0092\u0090")
        buf.write(u"\3\2\2\2\u0093\u0094\7\16\2\2\u0094\25\3\2\2\2\u0095")
        buf.write(u"\u0096\7\f\2\2\u0096\u009b\5\24\13\2\u0097\u0098\7\r")
        buf.write(u"\2\2\u0098\u009a\5\24\13\2\u0099\u0097\3\2\2\2\u009a")
        buf.write(u"\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2")
        buf.write(u"\2\u009c\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f")
        buf.write(u"\7\16\2\2\u009f\27\3\2\2\2\u00a0\u00a1\7\17\2\2\u00a1")
        buf.write(u"\u00a3\5\32\16\2\u00a2\u00a4\7$\2\2\u00a3\u00a2\3\2\2")
        buf.write(u"\2\u00a3\u00a4\3\2\2\2\u00a4\u00af\3\2\2\2\u00a5\u00a7")
        buf.write(u"\7\r\2\2\u00a6\u00a8\7$\2\2\u00a7\u00a6\3\2\2\2\u00a7")
        buf.write(u"\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab\5\32\16")
        buf.write(u"\2\u00aa\u00ac\7$\2\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac")
        buf.write(u"\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00a5\3\2\2\2\u00ae")
        buf.write(u"\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2")
        buf.write(u"\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b3")
        buf.write(u"\7\20\2\2\u00b3\u00b7\3\2\2\2\u00b4\u00b5\7\17\2\2\u00b5")
        buf.write(u"\u00b7\7\20\2\2\u00b6\u00a0\3\2\2\2\u00b6\u00b4\3\2\2")
        buf.write(u"\2\u00b7\31\3\2\2\2\u00b8\u00ba\7#\2\2\u00b9\u00bb\5")
        buf.write(u"\34\17\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write(u"\u00cc\3\2\2\2\u00bc\u00be\7\"\2\2\u00bd\u00bf\5\34\17")
        buf.write(u"\2\u00be\u00bd\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00cc")
        buf.write(u"\3\2\2\2\u00c0\u00c2\7 \2\2\u00c1\u00c3\5\34\17\2\u00c2")
        buf.write(u"\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00cc\3\2\2")
        buf.write(u"\2\u00c4\u00c6\7!\2\2\u00c5\u00c7\5\34\17\2\u00c6\u00c5")
        buf.write(u"\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00cc\3\2\2\2\u00c8")
        buf.write(u"\u00cc\7\35\2\2\u00c9\u00cc\7\37\2\2\u00ca\u00cc\7\36")
        buf.write(u"\2\2\u00cb\u00b8\3\2\2\2\u00cb\u00bc\3\2\2\2\u00cb\u00c0")
        buf.write(u"\3\2\2\2\u00cb\u00c4\3\2\2\2\u00cb\u00c8\3\2\2\2\u00cb")
        buf.write(u"\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\33\3\2\2\2\u00cd")
        buf.write(u"\u00ce\7\21\2\2\u00ce\u00d3\5\36\20\2\u00cf\u00d0\t\4")
        buf.write(u"\2\2\u00d0\u00d2\5\36\20\2\u00d1\u00cf\3\2\2\2\u00d2")
        buf.write(u"\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2")
        buf.write(u"\2\u00d4\u00d6\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7")
        buf.write(u"\7\24\2\2\u00d7\35\3\2\2\2\u00d8\u00db\7\35\2\2\u00d9")
        buf.write(u"\u00da\7\25\2\2\u00da\u00dc\7#\2\2\u00db\u00d9\3\2\2")
        buf.write(u"\2\u00db\u00dc\3\2\2\2\u00dc\37\3\2\2\2\u00dd\u00de\7")
        buf.write(u"\35\2\2\u00de!\3\2\2\2\"%\'.\64:@DOZ`bhntv|\u0082\u0088")
        buf.write(u"\u0090\u009b\u00a3\u00a7\u00ab\u00af\u00b6\u00ba\u00be")
        buf.write(u"\u00c2\u00c6\u00cb\u00d3\u00db")
        return buf.getvalue()


class ODLv21Parser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'END'", u"'end'", u"'='", u"':'", u"'^'", 
                     u"'OBJECT'", u"'END_OBJECT'", u"'GROUP'", u"'END_GROUP'", 
                     u"'('", u"','", u"')'", u"'{'", u"'}'", u"'<'", u"'*'", 
                     u"'/'", u"'>'", u"'**'", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'\r\n'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"DATE", u"TIME", u"YEAR_MONTH_DAY", u"YEAR_DOY", 
                      u"HH_MM_SS", u"DATE_TIME", u"SIGN", u"IDENTIFIER", 
                      u"STRING", u"SYMBOL_STRING", u"FLOAT", u"SCALED_REAL", 
                      u"BASED_INTEGER", u"INTEGER", u"NEWLINE", u"COMMENT", 
                      u"WS" ]

    RULE_label = 0
    RULE_statement = 1
    RULE_assignment_stmt = 2
    RULE_pointer_stmt = 3
    RULE_object_stmt = 4
    RULE_group_stmt = 5
    RULE_value = 6
    RULE_date_time_value = 7
    RULE_sequence_value = 8
    RULE_sequence_1D = 9
    RULE_sequence_2D = 10
    RULE_set_value = 11
    RULE_scalar_value = 12
    RULE_units_expression = 13
    RULE_units_factor = 14
    RULE_namespace_identifier = 15

    ruleNames =  [ u"label", u"statement", u"assignment_stmt", u"pointer_stmt", 
                   u"object_stmt", u"group_stmt", u"value", u"date_time_value", 
                   u"sequence_value", u"sequence_1D", u"sequence_2D", u"set_value", 
                   u"scalar_value", u"units_expression", u"units_factor", 
                   u"namespace_identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    DATE=20
    TIME=21
    YEAR_MONTH_DAY=22
    YEAR_DOY=23
    HH_MM_SS=24
    DATE_TIME=25
    SIGN=26
    IDENTIFIER=27
    STRING=28
    SYMBOL_STRING=29
    FLOAT=30
    SCALED_REAL=31
    BASED_INTEGER=32
    INTEGER=33
    NEWLINE=34
    COMMENT=35
    WS=36

    def __init__(self, input):
        super(ODLv21Parser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.LabelContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ODLv21Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ODLv21Parser.StatementContext,i)


        def COMMENT(self, i=None):
            if i is None:
                return self.getTokens(ODLv21Parser.COMMENT)
            else:
                return self.getToken(ODLv21Parser.COMMENT, i)

        def NEWLINE(self, i=None):
            if i is None:
                return self.getTokens(ODLv21Parser.NEWLINE)
            else:
                return self.getToken(ODLv21Parser.NEWLINE, i)

        def getRuleIndex(self):
            return ODLv21Parser.RULE_label

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterLabel(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitLabel(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = ODLv21Parser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ODLv21Parser.T__4) | (1 << ODLv21Parser.T__5) | (1 << ODLv21Parser.T__7) | (1 << ODLv21Parser.IDENTIFIER) | (1 << ODLv21Parser.NEWLINE) | (1 << ODLv21Parser.COMMENT))) != 0):
                self.state = 35
                token = self._input.LA(1)
                if token in [ODLv21Parser.T__4, ODLv21Parser.T__5, ODLv21Parser.T__7, ODLv21Parser.IDENTIFIER]:
                    self.state = 32
                    self.statement()

                elif token in [ODLv21Parser.COMMENT]:
                    self.state = 33
                    self.match(ODLv21Parser.COMMENT)

                elif token in [ODLv21Parser.NEWLINE]:
                    self.state = 34
                    self.match(ODLv21Parser.NEWLINE)

                else:
                    raise NoViableAltException(self)

                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            _la = self._input.LA(1)
            if not(_la==ODLv21Parser.T__0 or _la==ODLv21Parser.T__1):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignment_stmt(self):
            return self.getTypedRuleContext(ODLv21Parser.Assignment_stmtContext,0)


        def NEWLINE(self):
            return self.getToken(ODLv21Parser.NEWLINE, 0)

        def COMMENT(self):
            return self.getToken(ODLv21Parser.COMMENT, 0)

        def pointer_stmt(self):
            return self.getTypedRuleContext(ODLv21Parser.Pointer_stmtContext,0)


        def object_stmt(self):
            return self.getTypedRuleContext(ODLv21Parser.Object_stmtContext,0)


        def group_stmt(self):
            return self.getTypedRuleContext(ODLv21Parser.Group_stmtContext,0)


        def getRuleIndex(self):
            return ODLv21Parser.RULE_statement

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ODLv21Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 66
            token = self._input.LA(1)
            if token in [ODLv21Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.assignment_stmt()
                self.state = 44
                _la = self._input.LA(1)
                if _la==ODLv21Parser.COMMENT:
                    self.state = 43
                    self.match(ODLv21Parser.COMMENT)


                self.state = 46
                self.match(ODLv21Parser.NEWLINE)

            elif token in [ODLv21Parser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.pointer_stmt()
                self.state = 50
                _la = self._input.LA(1)
                if _la==ODLv21Parser.COMMENT:
                    self.state = 49
                    self.match(ODLv21Parser.COMMENT)


                self.state = 52
                self.match(ODLv21Parser.NEWLINE)

            elif token in [ODLv21Parser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.object_stmt()
                self.state = 56
                _la = self._input.LA(1)
                if _la==ODLv21Parser.COMMENT:
                    self.state = 55
                    self.match(ODLv21Parser.COMMENT)


                self.state = 58
                self.match(ODLv21Parser.NEWLINE)

            elif token in [ODLv21Parser.T__7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.group_stmt()
                self.state = 62
                _la = self._input.LA(1)
                if _la==ODLv21Parser.COMMENT:
                    self.state = 61
                    self.match(ODLv21Parser.COMMENT)


                self.state = 64
                self.match(ODLv21Parser.NEWLINE)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignment_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Assignment_stmtContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ODLv21Parser.IDENTIFIER, 0)

        def value(self):
            return self.getTypedRuleContext(ODLv21Parser.ValueContext,0)


        def namespace_identifier(self):
            return self.getTypedRuleContext(ODLv21Parser.Namespace_identifierContext,0)


        def getRuleIndex(self):
            return ODLv21Parser.RULE_assignment_stmt

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterAssignment_stmt(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitAssignment_stmt(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = ODLv21Parser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment_stmt)
        try:
            self.state = 77
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(ODLv21Parser.IDENTIFIER)
                self.state = 69
                self.match(ODLv21Parser.T__2)
                self.state = 70
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.namespace_identifier()
                self.state = 72
                self.match(ODLv21Parser.T__3)
                self.state = 73
                self.match(ODLv21Parser.IDENTIFIER)
                self.state = 74
                self.match(ODLv21Parser.T__2)
                self.state = 75
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pointer_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Pointer_stmtContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ODLv21Parser.IDENTIFIER, 0)

        def value(self):
            return self.getTypedRuleContext(ODLv21Parser.ValueContext,0)


        def getRuleIndex(self):
            return ODLv21Parser.RULE_pointer_stmt

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterPointer_stmt(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitPointer_stmt(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitPointer_stmt(self)
            else:
                return visitor.visitChildren(self)




    def pointer_stmt(self):

        localctx = ODLv21Parser.Pointer_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pointer_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(ODLv21Parser.T__4)
            self.state = 80
            self.match(ODLv21Parser.IDENTIFIER)
            self.state = 81
            self.match(ODLv21Parser.T__2)
            self.state = 82
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Object_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Object_stmtContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i=None):
            if i is None:
                return self.getTokens(ODLv21Parser.IDENTIFIER)
            else:
                return self.getToken(ODLv21Parser.IDENTIFIER, i)

        def NEWLINE(self, i=None):
            if i is None:
                return self.getTokens(ODLv21Parser.NEWLINE)
            else:
                return self.getToken(ODLv21Parser.NEWLINE, i)

        def COMMENT(self, i=None):
            if i is None:
                return self.getTokens(ODLv21Parser.COMMENT)
            else:
                return self.getToken(ODLv21Parser.COMMENT, i)

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ODLv21Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ODLv21Parser.StatementContext,i)


        def getRuleIndex(self):
            return ODLv21Parser.RULE_object_stmt

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterObject_stmt(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitObject_stmt(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitObject_stmt(self)
            else:
                return visitor.visitChildren(self)




    def object_stmt(self):

        localctx = ODLv21Parser.Object_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_object_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(ODLv21Parser.T__5)
            self.state = 85
            self.match(ODLv21Parser.T__2)
            self.state = 86
            self.match(ODLv21Parser.IDENTIFIER)
            self.state = 88
            _la = self._input.LA(1)
            if _la==ODLv21Parser.COMMENT:
                self.state = 87
                self.match(ODLv21Parser.COMMENT)


            self.state = 90
            self.match(ODLv21Parser.NEWLINE)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ODLv21Parser.T__4) | (1 << ODLv21Parser.T__5) | (1 << ODLv21Parser.T__7) | (1 << ODLv21Parser.IDENTIFIER) | (1 << ODLv21Parser.NEWLINE) | (1 << ODLv21Parser.COMMENT))) != 0):
                self.state = 94
                token = self._input.LA(1)
                if token in [ODLv21Parser.T__4, ODLv21Parser.T__5, ODLv21Parser.T__7, ODLv21Parser.IDENTIFIER]:
                    self.state = 91
                    self.statement()

                elif token in [ODLv21Parser.COMMENT]:
                    self.state = 92
                    self.match(ODLv21Parser.COMMENT)

                elif token in [ODLv21Parser.NEWLINE]:
                    self.state = 93
                    self.match(ODLv21Parser.NEWLINE)

                else:
                    raise NoViableAltException(self)

                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self.match(ODLv21Parser.T__6)
            self.state = 102
            _la = self._input.LA(1)
            if _la==ODLv21Parser.T__2:
                self.state = 100
                self.match(ODLv21Parser.T__2)
                self.state = 101
                self.match(ODLv21Parser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Group_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Group_stmtContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i=None):
            if i is None:
                return self.getTokens(ODLv21Parser.IDENTIFIER)
            else:
                return self.getToken(ODLv21Parser.IDENTIFIER, i)

        def NEWLINE(self, i=None):
            if i is None:
                return self.getTokens(ODLv21Parser.NEWLINE)
            else:
                return self.getToken(ODLv21Parser.NEWLINE, i)

        def COMMENT(self, i=None):
            if i is None:
                return self.getTokens(ODLv21Parser.COMMENT)
            else:
                return self.getToken(ODLv21Parser.COMMENT, i)

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ODLv21Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ODLv21Parser.StatementContext,i)


        def getRuleIndex(self):
            return ODLv21Parser.RULE_group_stmt

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterGroup_stmt(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitGroup_stmt(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitGroup_stmt(self)
            else:
                return visitor.visitChildren(self)




    def group_stmt(self):

        localctx = ODLv21Parser.Group_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_group_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(ODLv21Parser.T__7)
            self.state = 105
            self.match(ODLv21Parser.T__2)
            self.state = 106
            self.match(ODLv21Parser.IDENTIFIER)
            self.state = 108
            _la = self._input.LA(1)
            if _la==ODLv21Parser.COMMENT:
                self.state = 107
                self.match(ODLv21Parser.COMMENT)


            self.state = 110
            self.match(ODLv21Parser.NEWLINE)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ODLv21Parser.T__4) | (1 << ODLv21Parser.T__5) | (1 << ODLv21Parser.T__7) | (1 << ODLv21Parser.IDENTIFIER) | (1 << ODLv21Parser.NEWLINE) | (1 << ODLv21Parser.COMMENT))) != 0):
                self.state = 114
                token = self._input.LA(1)
                if token in [ODLv21Parser.T__4, ODLv21Parser.T__5, ODLv21Parser.T__7, ODLv21Parser.IDENTIFIER]:
                    self.state = 111
                    self.statement()

                elif token in [ODLv21Parser.COMMENT]:
                    self.state = 112
                    self.match(ODLv21Parser.COMMENT)

                elif token in [ODLv21Parser.NEWLINE]:
                    self.state = 113
                    self.match(ODLv21Parser.NEWLINE)

                else:
                    raise NoViableAltException(self)

                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self.match(ODLv21Parser.T__8)
            self.state = 122
            _la = self._input.LA(1)
            if _la==ODLv21Parser.T__2:
                self.state = 120
                self.match(ODLv21Parser.T__2)
                self.state = 121
                self.match(ODLv21Parser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.ValueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def scalar_value(self):
            return self.getTypedRuleContext(ODLv21Parser.Scalar_valueContext,0)


        def sequence_value(self):
            return self.getTypedRuleContext(ODLv21Parser.Sequence_valueContext,0)


        def set_value(self):
            return self.getTypedRuleContext(ODLv21Parser.Set_valueContext,0)


        def date_time_value(self):
            return self.getTypedRuleContext(ODLv21Parser.Date_time_valueContext,0)


        def getRuleIndex(self):
            return ODLv21Parser.RULE_value

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterValue(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitValue(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = ODLv21Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        try:
            self.state = 128
            token = self._input.LA(1)
            if token in [ODLv21Parser.IDENTIFIER, ODLv21Parser.STRING, ODLv21Parser.SYMBOL_STRING, ODLv21Parser.FLOAT, ODLv21Parser.SCALED_REAL, ODLv21Parser.BASED_INTEGER, ODLv21Parser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.scalar_value()

            elif token in [ODLv21Parser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.sequence_value()

            elif token in [ODLv21Parser.T__12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.set_value()

            elif token in [ODLv21Parser.DATE, ODLv21Parser.TIME, ODLv21Parser.DATE_TIME]:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.date_time_value()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Date_time_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Date_time_valueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(ODLv21Parser.DATE, 0)

        def TIME(self):
            return self.getToken(ODLv21Parser.TIME, 0)

        def DATE_TIME(self):
            return self.getToken(ODLv21Parser.DATE_TIME, 0)

        def getRuleIndex(self):
            return ODLv21Parser.RULE_date_time_value

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterDate_time_value(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitDate_time_value(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitDate_time_value(self)
            else:
                return visitor.visitChildren(self)




    def date_time_value(self):

        localctx = ODLv21Parser.Date_time_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_date_time_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ODLv21Parser.DATE) | (1 << ODLv21Parser.TIME) | (1 << ODLv21Parser.DATE_TIME))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sequence_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Sequence_valueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def sequence_1D(self):
            return self.getTypedRuleContext(ODLv21Parser.Sequence_1DContext,0)


        def sequence_2D(self):
            return self.getTypedRuleContext(ODLv21Parser.Sequence_2DContext,0)


        def getRuleIndex(self):
            return ODLv21Parser.RULE_sequence_value

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterSequence_value(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitSequence_value(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitSequence_value(self)
            else:
                return visitor.visitChildren(self)




    def sequence_value(self):

        localctx = ODLv21Parser.Sequence_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_sequence_value)
        try:
            self.state = 134
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.sequence_1D()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.sequence_2D()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sequence_1DContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Sequence_1DContext, self).__init__(parent, invokingState)
            self.parser = parser

        def scalar_value(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ODLv21Parser.Scalar_valueContext)
            else:
                return self.getTypedRuleContext(ODLv21Parser.Scalar_valueContext,i)


        def getRuleIndex(self):
            return ODLv21Parser.RULE_sequence_1D

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterSequence_1D(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitSequence_1D(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitSequence_1D(self)
            else:
                return visitor.visitChildren(self)




    def sequence_1D(self):

        localctx = ODLv21Parser.Sequence_1DContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_sequence_1D)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(ODLv21Parser.T__9)
            self.state = 137
            self.scalar_value()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ODLv21Parser.T__10:
                self.state = 138
                self.match(ODLv21Parser.T__10)
                self.state = 139
                self.scalar_value()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self.match(ODLv21Parser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sequence_2DContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Sequence_2DContext, self).__init__(parent, invokingState)
            self.parser = parser

        def sequence_1D(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ODLv21Parser.Sequence_1DContext)
            else:
                return self.getTypedRuleContext(ODLv21Parser.Sequence_1DContext,i)


        def getRuleIndex(self):
            return ODLv21Parser.RULE_sequence_2D

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterSequence_2D(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitSequence_2D(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitSequence_2D(self)
            else:
                return visitor.visitChildren(self)




    def sequence_2D(self):

        localctx = ODLv21Parser.Sequence_2DContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sequence_2D)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(ODLv21Parser.T__9)
            self.state = 148
            self.sequence_1D()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ODLv21Parser.T__10:
                self.state = 149
                self.match(ODLv21Parser.T__10)
                self.state = 150
                self.sequence_1D()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.match(ODLv21Parser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Set_valueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def scalar_value(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ODLv21Parser.Scalar_valueContext)
            else:
                return self.getTypedRuleContext(ODLv21Parser.Scalar_valueContext,i)


        def NEWLINE(self, i=None):
            if i is None:
                return self.getTokens(ODLv21Parser.NEWLINE)
            else:
                return self.getToken(ODLv21Parser.NEWLINE, i)

        def getRuleIndex(self):
            return ODLv21Parser.RULE_set_value

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterSet_value(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitSet_value(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitSet_value(self)
            else:
                return visitor.visitChildren(self)




    def set_value(self):

        localctx = ODLv21Parser.Set_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_set_value)
        self._la = 0 # Token type
        try:
            self.state = 180
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(ODLv21Parser.T__12)
                self.state = 159
                self.scalar_value()
                self.state = 161
                _la = self._input.LA(1)
                if _la==ODLv21Parser.NEWLINE:
                    self.state = 160
                    self.match(ODLv21Parser.NEWLINE)


                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ODLv21Parser.T__10:
                    self.state = 163
                    self.match(ODLv21Parser.T__10)
                    self.state = 165
                    _la = self._input.LA(1)
                    if _la==ODLv21Parser.NEWLINE:
                        self.state = 164
                        self.match(ODLv21Parser.NEWLINE)


                    self.state = 167
                    self.scalar_value()
                    self.state = 169
                    _la = self._input.LA(1)
                    if _la==ODLv21Parser.NEWLINE:
                        self.state = 168
                        self.match(ODLv21Parser.NEWLINE)


                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 176
                self.match(ODLv21Parser.T__13)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(ODLv21Parser.T__12)
                self.state = 179
                self.match(ODLv21Parser.T__13)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Scalar_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Scalar_valueContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ODLv21Parser.RULE_scalar_value

     
        def copyFrom(self, ctx):
            super(ODLv21Parser.Scalar_valueContext, self).copyFrom(ctx)



    class ScalarStringContext(Scalar_valueContext):

        def __init__(self, parser, ctx): # actually a ODLv21Parser.Scalar_valueContext)
            super(ODLv21Parser.ScalarStringContext, self).__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ODLv21Parser.STRING, 0)

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterScalarString(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitScalarString(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitScalarString(self)
            else:
                return visitor.visitChildren(self)


    class ScalarIntegerContext(Scalar_valueContext):

        def __init__(self, parser, ctx): # actually a ODLv21Parser.Scalar_valueContext)
            super(ODLv21Parser.ScalarIntegerContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(ODLv21Parser.INTEGER, 0)
        def units_expression(self):
            return self.getTypedRuleContext(ODLv21Parser.Units_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterScalarInteger(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitScalarInteger(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitScalarInteger(self)
            else:
                return visitor.visitChildren(self)


    class ScalarIdentifierContext(Scalar_valueContext):

        def __init__(self, parser, ctx): # actually a ODLv21Parser.Scalar_valueContext)
            super(ODLv21Parser.ScalarIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ODLv21Parser.IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterScalarIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitScalarIdentifier(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitScalarIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class ScalarBasedIntegerContext(Scalar_valueContext):

        def __init__(self, parser, ctx): # actually a ODLv21Parser.Scalar_valueContext)
            super(ODLv21Parser.ScalarBasedIntegerContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BASED_INTEGER(self):
            return self.getToken(ODLv21Parser.BASED_INTEGER, 0)
        def units_expression(self):
            return self.getTypedRuleContext(ODLv21Parser.Units_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterScalarBasedInteger(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitScalarBasedInteger(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitScalarBasedInteger(self)
            else:
                return visitor.visitChildren(self)


    class ScalarScaledRealContext(Scalar_valueContext):

        def __init__(self, parser, ctx): # actually a ODLv21Parser.Scalar_valueContext)
            super(ODLv21Parser.ScalarScaledRealContext, self).__init__(parser)
            self.copyFrom(ctx)

        def SCALED_REAL(self):
            return self.getToken(ODLv21Parser.SCALED_REAL, 0)
        def units_expression(self):
            return self.getTypedRuleContext(ODLv21Parser.Units_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterScalarScaledReal(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitScalarScaledReal(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitScalarScaledReal(self)
            else:
                return visitor.visitChildren(self)


    class ScalarSymbolContext(Scalar_valueContext):

        def __init__(self, parser, ctx): # actually a ODLv21Parser.Scalar_valueContext)
            super(ODLv21Parser.ScalarSymbolContext, self).__init__(parser)
            self.copyFrom(ctx)

        def SYMBOL_STRING(self):
            return self.getToken(ODLv21Parser.SYMBOL_STRING, 0)

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterScalarSymbol(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitScalarSymbol(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitScalarSymbol(self)
            else:
                return visitor.visitChildren(self)


    class ScalarFloatContext(Scalar_valueContext):

        def __init__(self, parser, ctx): # actually a ODLv21Parser.Scalar_valueContext)
            super(ODLv21Parser.ScalarFloatContext, self).__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(ODLv21Parser.FLOAT, 0)
        def units_expression(self):
            return self.getTypedRuleContext(ODLv21Parser.Units_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterScalarFloat(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitScalarFloat(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitScalarFloat(self)
            else:
                return visitor.visitChildren(self)



    def scalar_value(self):

        localctx = ODLv21Parser.Scalar_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_scalar_value)
        self._la = 0 # Token type
        try:
            self.state = 201
            token = self._input.LA(1)
            if token in [ODLv21Parser.INTEGER]:
                localctx = ODLv21Parser.ScalarIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(ODLv21Parser.INTEGER)
                self.state = 184
                _la = self._input.LA(1)
                if _la==ODLv21Parser.T__14:
                    self.state = 183
                    self.units_expression()



            elif token in [ODLv21Parser.BASED_INTEGER]:
                localctx = ODLv21Parser.ScalarBasedIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(ODLv21Parser.BASED_INTEGER)
                self.state = 188
                _la = self._input.LA(1)
                if _la==ODLv21Parser.T__14:
                    self.state = 187
                    self.units_expression()



            elif token in [ODLv21Parser.FLOAT]:
                localctx = ODLv21Parser.ScalarFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.match(ODLv21Parser.FLOAT)
                self.state = 192
                _la = self._input.LA(1)
                if _la==ODLv21Parser.T__14:
                    self.state = 191
                    self.units_expression()



            elif token in [ODLv21Parser.SCALED_REAL]:
                localctx = ODLv21Parser.ScalarScaledRealContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.match(ODLv21Parser.SCALED_REAL)
                self.state = 196
                _la = self._input.LA(1)
                if _la==ODLv21Parser.T__14:
                    self.state = 195
                    self.units_expression()



            elif token in [ODLv21Parser.IDENTIFIER]:
                localctx = ODLv21Parser.ScalarIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 198
                self.match(ODLv21Parser.IDENTIFIER)

            elif token in [ODLv21Parser.SYMBOL_STRING]:
                localctx = ODLv21Parser.ScalarSymbolContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 199
                self.match(ODLv21Parser.SYMBOL_STRING)

            elif token in [ODLv21Parser.STRING]:
                localctx = ODLv21Parser.ScalarStringContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 200
                self.match(ODLv21Parser.STRING)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Units_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Units_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def units_factor(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ODLv21Parser.Units_factorContext)
            else:
                return self.getTypedRuleContext(ODLv21Parser.Units_factorContext,i)


        def getRuleIndex(self):
            return ODLv21Parser.RULE_units_expression

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterUnits_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitUnits_expression(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitUnits_expression(self)
            else:
                return visitor.visitChildren(self)




    def units_expression(self):

        localctx = ODLv21Parser.Units_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_units_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(ODLv21Parser.T__14)
            self.state = 204
            self.units_factor()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ODLv21Parser.T__15 or _la==ODLv21Parser.T__16:
                self.state = 205
                _la = self._input.LA(1)
                if not(_la==ODLv21Parser.T__15 or _la==ODLv21Parser.T__16):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 206
                self.units_factor()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.match(ODLv21Parser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Units_factorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Units_factorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ODLv21Parser.IDENTIFIER, 0)

        def INTEGER(self):
            return self.getToken(ODLv21Parser.INTEGER, 0)

        def getRuleIndex(self):
            return ODLv21Parser.RULE_units_factor

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterUnits_factor(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitUnits_factor(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitUnits_factor(self)
            else:
                return visitor.visitChildren(self)




    def units_factor(self):

        localctx = ODLv21Parser.Units_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_units_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ODLv21Parser.IDENTIFIER)
            self.state = 217
            _la = self._input.LA(1)
            if _la==ODLv21Parser.T__18:
                self.state = 215
                self.match(ODLv21Parser.T__18)
                self.state = 216
                self.match(ODLv21Parser.INTEGER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Namespace_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ODLv21Parser.Namespace_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ODLv21Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ODLv21Parser.RULE_namespace_identifier

        def enterRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.enterNamespace_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, ODLv21Listener ):
                listener.exitNamespace_identifier(self)

        def accept(self, visitor):
            if isinstance( visitor, ODLv21Visitor ):
                return visitor.visitNamespace_identifier(self)
            else:
                return visitor.visitChildren(self)




    def namespace_identifier(self):

        localctx = ODLv21Parser.Namespace_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_namespace_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(ODLv21Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




