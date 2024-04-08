# Generated from test.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .testParser import testParser
else:
    from testParser import testParser

# This class defines a complete listener for a parse tree produced by testParser.
class testListener(ParseTreeListener):

    # Enter a parse tree produced by testParser#init.
    def enterInit(self, ctx:testParser.InitContext):
        pass

    # Exit a parse tree produced by testParser#init.
    def exitInit(self, ctx:testParser.InitContext):
        pass


    # Enter a parse tree produced by testParser#value.
    def enterValue(self, ctx:testParser.ValueContext):
        pass

    # Exit a parse tree produced by testParser#value.
    def exitValue(self, ctx:testParser.ValueContext):
        pass



del testParser