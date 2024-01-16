def solution(a, b):
    result1 = 2*a*b
    result2 = int(str(a)+str(b))
    
    if(result1 < result2): return result2
    return result1