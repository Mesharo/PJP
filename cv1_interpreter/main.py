def removeSpaces(expression : str) -> str:
    return ("".join(expression.split(" ")))

def isOperatorOrParenthesis(character : str) -> bool:
    return (character in ("+", "-", "*", "/", "(", ")"))

def invalidCharacters(modifiedExpression : str):
    """
    Function doublechecks the arithmetic expression follows the rules in README.
    If not, interpreter is stopped.
    """
    for character in modifiedExpression:
        if not(character.isdigit() or isOperatorOrParenthesis(character)):
            return True
    return False

def unbalancedParentheses(expression : str) -> bool:
    """
    Function checks if the parity of parentheses in the expression is correct.
    """
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
    """
    Function checks if expression contains empty parentheses.
    """
    for index, character in enumerate(expression):
        if (character == "("):
            if not(expression[index + 1].isdigit() or expression[index + 1] == "("):
                return True
    return False

def wrongConnection(expression : str) -> bool:
    """
    Function makes sure each character in the expression is both followed by an appropriate symbol,
    and its predecessor is an approprite symbol.

    Correct follow-ups:

        ( -> Before: operator, (
             After: checked in emptyParentheses

        ) -> Before: number, )
             After: operator, )

        number -> Before: number, operator, (
                  After: number, operator, )

        op -> Before: number, )
              After: number, (
    """
    operators = ("+", "-", "*", "/")

    # parentheses checked before, numbers are fine
    if ((expression[0] in operators) or (expression[len(expression) - 1] in operators)):
        return True 

    for index, character in enumerate(expression):
        if (index == 0 or index == len(expression) - 1):
            continue

        if (character == "("):
            if not((expression[index - 1] in operators) or (expression[index - 1] == "(")):
                return True
        elif (character == ")"):
            if not((expression[index - 1].isdigit()) or (expression[index - 1] == ")")):
                return True
            if not((expression[index + 1] in operators) or (expression[index + 1] == ")")):
                return True
        elif (character.isdigit()):
            if (expression[index - 1] == ")"):
                return True
            if (expression[index + 1] == "("):
                return True
        else:
            if not((expression[index - 1].isdigit()) or (expression[index - 1] == ")")):
                return True
            if not((expression[index + 1].isdigit()) or (expression[index + 1] == "(")):
                return True
    return False

def solvable(expression : str) -> bool:
    """
    Function makes sure the expression follows syntax rules before it's processed.
    """
    modifiedExpression = removeSpaces(expression)

    if (invalidCharacters(modifiedExpression)):
        return False

    if (unbalancedParentheses(modifiedExpression)):
        return False
    
    if (emptyParentheses(modifiedExpression)):
        return False
    
    if (wrongConnection(modifiedExpression)):
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