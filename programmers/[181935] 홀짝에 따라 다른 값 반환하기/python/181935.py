def solution(n):
    result = 0
    if(n%2 == 0):
        for i in range(2,n+1,2):
            result += (i*i)
    elif(n%2 == 1):
        for i in range(1, n+1, 2):
            result += i
    return result