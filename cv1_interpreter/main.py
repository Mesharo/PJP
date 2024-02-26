def modify(expression : str) -> str:
    pass

def solvable(expression : str) -> bool:
    return True

def solve(expression : str) -> None:
    if solvable(expression):
        print(eval(expression))
    else:
        print("ERROR")
    
if __name__ == "__main__":
    for __ in range(int(input())):
        solve(input())