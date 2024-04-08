def solve(expression : str) -> None:
    tokens = {
        "+": "OP",
        "-": "OP",
        "*": "OP",
        "/": "OP",
        "(": "LPAR",
        ")": "RPAR",
        ";": "SEMICOLON"
    }

    foundComment = False
    foundWord = False
    currentWord = ""

    for index, character in enumerate(expression):
        if (foundComment is True):
            if (character == "\n"):
                foundComment = False
            continue

        if (character.isdigit()):
            print(f'NUM:{character}')
            continue

        if (character.isalpha()):
            pass      

        print(f'{tokens[character]}:{character}')

if __name__ == "__main__":
    #solve(input())

    xd = "abcdefedcba"

    print(xd == xd[::-1])