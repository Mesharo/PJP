from antlr4 import *
from projektLanguageLexer import projektLanguageLexer
from projektLanguageParser import projektLanguageParser

contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
input_text = '\n'.join(contents)

lexer = projektLanguageLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = projektLanguageParser(stream)

tree = parser.program()

print(tree.toStringTree(recog=parser))