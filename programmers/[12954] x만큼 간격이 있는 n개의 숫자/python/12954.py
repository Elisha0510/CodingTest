def solution(x, n):
    result = []
    
    if(x == 0):
        for i in range(n):
            result.append(0)
    else:
        for i in range(x, x*n+x, x):
            result.append(i)
            if(len(result) == n): break
            
    return result