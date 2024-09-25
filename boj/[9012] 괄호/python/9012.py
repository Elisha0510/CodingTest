import sys

n = int(sys.stdin.readline().strip())

def VPS(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(string[i])
        else:
            length = len(stack)
            if length:
                stack.pop()
            else:
                return False
            
    if len(stack):
        return False
    return True

for i in range(n):
    string = list(sys.stdin.readline().strip())
    result = VPS(string)
    if result:
        print("YES")
    else:
        print("NO")