# Generated from projektLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .projektLanguageParser import projektLanguageParser
else:
    from projektLanguageParser import projektLanguageParser

# This class defines a complete listener for a parse tree produced by projektLanguageParser.
class projektLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by projektLanguageParser#program.
    def enterProgram(self, ctx:projektLanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by projektLanguageParser#program.
    def exitProgram(self, ctx:projektLanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by projektLanguageParser#statement.
    def enterStatement(self, ctx:projektLanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by projektLanguageParser#statement.
    def exitStatement(self, ctx:projektLanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by projektLanguageParser#expression.
    def enterExpression(self, ctx:projektLanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by projektLanguageParser#expression.
    def exitExpression(self, ctx:projektLanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by projektLanguageParser#literal.
    def enterLiteral(self, ctx:projektLanguageParser.LiteralContext):
        pass

    # Exit a parse tree produced by projektLanguageParser#literal.
    def exitLiteral(self, ctx:projektLanguageParser.LiteralContext):
        pass



del projektLanguageParser