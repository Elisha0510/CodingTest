def solution(s):
    # 회전 - 슬라이싱
    arr = []
    cnt = 0
    for i in range(len(s)-1):
        result = examine(s)
        if(result): cnt+=1
        left = s[0]
        right = s[1:]
        arr = right + left
        s = arr
    
    return cnt
        
def examine(s):
    # 괄호 검사 - 스택
    stack = []
    for i in range(len(s)):
        flag = 0
        if(len(stack) == 0):
            stack.append(s[i])
        elif((stack[-1] == '[' and s[i] == ']') or (stack[-1] == '{' and s[i] == '}') or (stack[-1] == '(' and s[i] == ')')):
            flag = 1
            stack.pop()
        elif(flag == 0):
            stack.append(s[i])
        
    if(len(stack) == 0):
        return True
    else:
        return False
            
            
        
    
    