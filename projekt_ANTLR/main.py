from antlr4 import *
from projektLanguageLexer import projektLanguageLexer
from projektLanguageParser import projektLanguageParser


input_text = input("> ")
lexer = projektLanguageLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = projektLanguageParser(stream)

tree = parser.program()

print(tree.toStringTree(recog=parser))