from antlr4.error.ErrorListener import ErrorListener

class syntaxErrorListener( ErrorListener ):

    def __init__(self):
        super(syntaxErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f'--- --- ---\nSyntax error!\nRecognizer: {recognizer}\noffendingSymbol: {offendingSymbol}\nline: {line}\ncolumn: {column}\nmsg: {msg}\ne: {e}')