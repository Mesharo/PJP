# Generated from projektLanguage.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,113,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,35,8,1,10,1,12,1,38,9,1,1,1,
        1,1,1,1,1,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,1,1,1,1,1,1,
        5,1,55,8,1,10,1,12,1,58,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,69,8,1,1,1,3,1,72,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,86,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,106,8,2,10,2,12,2,109,9,2,1,3,1,
        3,1,3,0,1,4,4,0,2,4,6,0,7,1,0,22,25,1,0,7,8,1,0,9,11,2,0,8,8,12,
        13,1,0,14,15,1,0,16,17,1,0,31,34,131,0,9,1,0,0,0,2,71,1,0,0,0,4,
        85,1,0,0,0,6,110,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,
        11,9,1,0,0,0,11,12,1,0,0,0,12,13,1,0,0,0,13,14,5,0,0,1,14,1,1,0,
        0,0,15,72,5,1,0,0,16,20,5,2,0,0,17,19,3,2,1,0,18,17,1,0,0,0,19,22,
        1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,23,1,0,0,0,22,20,1,0,0,0,
        23,72,5,3,0,0,24,25,5,21,0,0,25,26,5,4,0,0,26,27,3,4,2,0,27,28,5,
        5,0,0,28,29,3,2,1,0,29,72,1,0,0,0,30,31,7,0,0,0,31,36,5,30,0,0,32,
        33,5,6,0,0,33,35,5,30,0,0,34,32,1,0,0,0,35,38,1,0,0,0,36,34,1,0,
        0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,39,72,5,1,0,0,40,41,
        5,26,0,0,41,46,5,30,0,0,42,43,5,6,0,0,43,45,5,30,0,0,44,42,1,0,0,
        0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,
        1,0,0,0,49,72,5,1,0,0,50,51,5,27,0,0,51,56,3,4,2,0,52,53,5,6,0,0,
        53,55,3,4,2,0,54,52,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,
        0,0,0,57,59,1,0,0,0,58,56,1,0,0,0,59,60,5,1,0,0,60,72,1,0,0,0,61,
        62,5,28,0,0,62,63,5,4,0,0,63,64,3,4,2,0,64,65,5,5,0,0,65,68,3,2,
        1,0,66,67,5,29,0,0,67,69,3,2,1,0,68,66,1,0,0,0,68,69,1,0,0,0,69,
        72,1,0,0,0,70,72,3,4,2,0,71,15,1,0,0,0,71,16,1,0,0,0,71,24,1,0,0,
        0,71,30,1,0,0,0,71,40,1,0,0,0,71,50,1,0,0,0,71,61,1,0,0,0,71,70,
        1,0,0,0,72,3,1,0,0,0,73,74,6,2,-1,0,74,75,5,4,0,0,75,76,3,4,2,0,
        76,77,5,5,0,0,77,86,1,0,0,0,78,86,5,30,0,0,79,86,3,6,3,0,80,81,7,
        1,0,0,81,86,3,4,2,8,82,83,5,30,0,0,83,84,5,20,0,0,84,86,3,4,2,1,
        85,73,1,0,0,0,85,78,1,0,0,0,85,79,1,0,0,0,85,80,1,0,0,0,85,82,1,
        0,0,0,86,107,1,0,0,0,87,88,10,7,0,0,88,89,7,2,0,0,89,106,3,4,2,8,
        90,91,10,6,0,0,91,92,7,3,0,0,92,106,3,4,2,7,93,94,10,5,0,0,94,95,
        7,4,0,0,95,106,3,4,2,6,96,97,10,4,0,0,97,98,7,5,0,0,98,106,3,4,2,
        5,99,100,10,3,0,0,100,101,5,18,0,0,101,106,3,4,2,4,102,103,10,2,
        0,0,103,104,5,19,0,0,104,106,3,4,2,3,105,87,1,0,0,0,105,90,1,0,0,
        0,105,93,1,0,0,0,105,96,1,0,0,0,105,99,1,0,0,0,105,102,1,0,0,0,106,
        109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,5,1,0,0,0,109,107,
        1,0,0,0,110,111,7,6,0,0,111,7,1,0,0,0,10,11,20,36,46,56,68,71,85,
        105,107
    ]

class projektLanguageParser ( Parser ):

    grammarFileName = "projektLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "'('", "')'", "','", 
                     "'!'", "'-'", "'*'", "'/'", "'%'", "'+'", "'.'", "'>'", 
                     "'<'", "'=='", "'!='", "'&&'", "'||'", "'='", "'while'", 
                     "'int'", "'float'", "'string'", "'bool'", "'read'", 
                     "'write'", "'if'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WHILE", "INT", "FLOAT", "STRING", "BOOL", 
                      "READ", "WRITE", "IF", "ELSE", "IDENTIFIER", "INT_LITERAL", 
                      "FLOAT_LITERAL", "BOOL_LITERAL", "STRING_LITERAL", 
                      "WS", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_literal = 3

    ruleNames =  [ "program", "statement", "expression", "literal" ]

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
    T__19=20
    WHILE=21
    INT=22
    FLOAT=23
    STRING=24
    BOOL=25
    READ=26
    WRITE=27
    IF=28
    ELSE=29
    IDENTIFIER=30
    INT_LITERAL=31
    FLOAT_LITERAL=32
    BOOL_LITERAL=33
    STRING_LITERAL=34
    WS=35
    LINE_COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(projektLanguageParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(projektLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(projektLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return projektLanguageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = projektLanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33820770710) != 0)):
                    break

            self.state = 13
            self.match(projektLanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(projektLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(projektLanguageParser.StatementContext,i)


        def WHILE(self):
            return self.getToken(projektLanguageParser.WHILE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(projektLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(projektLanguageParser.ExpressionContext,i)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(projektLanguageParser.IDENTIFIER)
            else:
                return self.getToken(projektLanguageParser.IDENTIFIER, i)

        def INT(self):
            return self.getToken(projektLanguageParser.INT, 0)

        def FLOAT(self):
            return self.getToken(projektLanguageParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(projektLanguageParser.STRING, 0)

        def BOOL(self):
            return self.getToken(projektLanguageParser.BOOL, 0)

        def READ(self):
            return self.getToken(projektLanguageParser.READ, 0)

        def WRITE(self):
            return self.getToken(projektLanguageParser.WRITE, 0)

        def IF(self):
            return self.getToken(projektLanguageParser.IF, 0)

        def ELSE(self):
            return self.getToken(projektLanguageParser.ELSE, 0)

        def getRuleIndex(self):
            return projektLanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = projektLanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(projektLanguageParser.T__0)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(projektLanguageParser.T__1)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33820770710) != 0):
                    self.state = 17
                    self.statement()
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 23
                self.match(projektLanguageParser.T__2)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.match(projektLanguageParser.WHILE)
                self.state = 25
                self.match(projektLanguageParser.T__3)
                self.state = 26
                self.expression(0)
                self.state = 27
                self.match(projektLanguageParser.T__4)
                self.state = 28
                self.statement()
                pass
            elif token in [22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 31
                self.match(projektLanguageParser.IDENTIFIER)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 32
                    self.match(projektLanguageParser.T__5)
                    self.state = 33
                    self.match(projektLanguageParser.IDENTIFIER)
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 39
                self.match(projektLanguageParser.T__0)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.match(projektLanguageParser.READ)
                self.state = 41
                self.match(projektLanguageParser.IDENTIFIER)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 42
                    self.match(projektLanguageParser.T__5)
                    self.state = 43
                    self.match(projektLanguageParser.IDENTIFIER)
                    self.state = 48
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 49
                self.match(projektLanguageParser.T__0)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.match(projektLanguageParser.WRITE)
                self.state = 51
                self.expression(0)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 52
                    self.match(projektLanguageParser.T__5)
                    self.state = 53
                    self.expression(0)
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 59
                self.match(projektLanguageParser.T__0)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 7)
                self.state = 61
                self.match(projektLanguageParser.IF)
                self.state = 62
                self.match(projektLanguageParser.T__3)
                self.state = 63
                self.expression(0)
                self.state = 64
                self.match(projektLanguageParser.T__4)
                self.state = 65
                self.statement()
                self.state = 68
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 66
                    self.match(projektLanguageParser.ELSE)
                    self.state = 67
                    self.statement()


                pass
            elif token in [4, 7, 8, 30, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 8)
                self.state = 70
                self.expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.prefix = None # Token
            self.bop = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(projektLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(projektLanguageParser.ExpressionContext,i)


        def IDENTIFIER(self):
            return self.getToken(projektLanguageParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(projektLanguageParser.LiteralContext,0)


        def getRuleIndex(self):
            return projektLanguageParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = projektLanguageParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 74
                self.match(projektLanguageParser.T__3)
                self.state = 75
                self.expression(0)
                self.state = 76
                self.match(projektLanguageParser.T__4)
                pass

            elif la_ == 2:
                self.state = 78
                self.match(projektLanguageParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.state = 79
                self.literal()
                pass

            elif la_ == 4:
                self.state = 80
                localctx.prefix = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    localctx.prefix = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 81
                self.expression(8)
                pass

            elif la_ == 5:
                self.state = 82
                self.match(projektLanguageParser.IDENTIFIER)
                self.state = 83
                self.match(projektLanguageParser.T__19)
                self.state = 84
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 105
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = projektLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 87
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 88
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 89
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = projektLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 90
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 91
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 12544) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 92
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = projektLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 93
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 94
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 95
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = projektLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 96
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 97
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 98
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = projektLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 99
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 100
                        localctx.bop = self.match(projektLanguageParser.T__17)
                        self.state = 101
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = projektLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 102
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 103
                        localctx.bop = self.match(projektLanguageParser.T__18)
                        self.state = 104
                        self.expression(3)
                        pass

             
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(projektLanguageParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(projektLanguageParser.FLOAT_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(projektLanguageParser.BOOL_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(projektLanguageParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return projektLanguageParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = projektLanguageParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




