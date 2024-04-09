from antlr4 import *
from projektLanguageLexer import projektLanguageLexer
from projektLanguageParser import projektLanguageParser
from syntaxErrorListener import syntaxErrorListener
from typeCheckVisitor import TypeCheckVisitor

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

myTree = parser.program()

if parser.getNumberOfSyntaxErrors() == 0:
    typeCheckVisitor = TypeCheckVisitor()
    result = typeCheckVisitor.visit(tree=myTree)

    print(myTree.toStringTree(recog=parser))