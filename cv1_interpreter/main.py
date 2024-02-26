def removeSpaces(expression : str) -> str:
    return ("".join(expression.split(" ")))

def isOperatorOrParenthesis(character : str) -> bool:
    return (character in ("+", "-", "*", "/", "(", ")"))

def invalidCharacters(modifiedExpression : str):
    for character in modifiedExpression:
        if not(character.isdigit() or isOperatorOrParenthesis(character)):
            return True
    return False

def unbalancedParentheses(expression : str) -> bool:
    balance = 0

    for character in expression:
        if (balance < 0):
            return True
        if (character == "("):
            balance += 1
        if (character == ")"):
            balance -= 1
    
    if (balance != 0):
        return True
    return False

def emptyParentheses(expression : str) -> bool:
    for index, character in enumerate(expression):
        if (character == "("):
            if not(expression[index + 1].isdigit() or expression[index + 1] == "("):
                return True
    return False

def wrongConnection(expression : str) -> bool:
    pass

def unaryOperators(expression : str) -> bool:
    pass

def solvable(expression : str) -> bool:
    modifiedExpression = removeSpaces(expression)

    if (invalidCharacters(modifiedExpression)):
        return False

    if (unbalancedParentheses(modifiedExpression)):
        return False
    
    if (emptyParentheses(modifiedExpression)):
        return False
    
    if (wrongConnection(modifiedExpression)):
        return False
    
    if (unaryOperators(modifiedExpression)):
        return False
    
    return True

def solve(expression : str) -> None:
    if (solvable(expression)):
        print(eval(expression))
    else:
        print("ERROR")
    
if __name__ == "__main__":
    for __ in range(int(input())):
        solve(input())