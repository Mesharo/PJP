from antlr4 import *
from projektLanguageLexer import projektLanguageLexer
from projektLanguageParser import projektLanguageParser
from syntaxErrorListener import syntaxErrorListener

contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
input_text = '\n'.join(contents)

lexer = projektLanguageLexer(InputStream(input_text))
lexer.removeErrorListeners()
lexer.addErrorListener(syntaxErrorListener())

stream = CommonTokenStream(lexer)

parser = projektLanguageParser(stream)
parser.removeErrorListeners()
parser.addErrorListener(syntaxErrorListener())

tree = parser.program()

if parser.getNumberOfSyntaxErrors() == 0:
    print(tree.toStringTree(recog=parser))