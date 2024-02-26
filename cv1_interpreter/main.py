def removeSpaces(expression : str) -> str:
    return ("".join(expression.split(" ")))

def isOperatorOrParenthesis(character : str) -> bool:
    return (character in ("+", "-", "*", "/", "(", ")"))

def invalidCharacters(modifiedExpression : str):
    for character in modifiedExpression:
        if not(character.isdigit() or isOperatorOrParenthesis(character)):
            return True
    return False

def solvable(expression : str) -> bool:
    modifiedExpression = removeSpaces(expression)

    if (invalidCharacters(modifiedExpression)):
        return False

    stack = []

    # TODO check parenthesis parity and no unary exps

    return True

def solve(expression : str) -> None:
    if (solvable(expression)):
        print(eval(expression))
    else:
        print("ERROR")
    
if __name__ == "__main__":
    for __ in range(int(input())):
        solve(input())