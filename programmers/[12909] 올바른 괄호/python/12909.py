def solution(s):
    stack = []
    list_str = list(s)
    for i in range(len(s)):
        if(list_str[i] == '('):
            stack.append('(')
        elif(list_str[i] == ')'):
            if(len(stack)):
                stack.pop()
            else:
                return False
            
    if(len(stack) == 0): return True
    return False