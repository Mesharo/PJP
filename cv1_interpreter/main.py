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


"""
Correct follow-ups

( -> Before: operator, (
     After: checked in emptyParentheses

) -> Before: number, )
     After: operator, )

number -> Before: number, operator, (
          After: number, operator, )

op -> Before: number, )
      After: number, (
"""
def wrongConnection(expression : str) -> bool:
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
            if not((expression[index - 1].isdigit()) or (expression[index - 1] in operators) or (expression[index - 1] == "(")):
                return True
            if not((expression[index + 1].isdigit()) or (expression[index + 1] in operators) or (expression[index + 1] == ")")):
                return True
        else:
            if not((expression[index - 1].isdigit()) or (expression[index - 1] == ")")):
                return True
            if not((expression[index + 1].isdigit()) or (expression[index + 1] == "(")):
                return True
    return False

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
    
    return True

def solve(expression : str) -> None:
    if (solvable(expression)):
        print(eval(expression))
    else:
        print("ERROR")
    
if __name__ == "__main__":
    for __ in range(int(input())):
        solve(input())