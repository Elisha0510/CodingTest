import sys

def isValid(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[':
            stack.append(string[i])
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif string[i] == "]":
            if len(stack) == 0:
                return False
            if stack[-1] == "[":
                stack.pop()
            else:
                return False
    
    if len(stack):
        return False
    return True
            

while 1:
    string = sys.stdin.readline()
    if string.strip() == "." and len(string) == 2:
        break
    result = isValid(string)
    if result:
        print("yes")
    else:
        print("no")