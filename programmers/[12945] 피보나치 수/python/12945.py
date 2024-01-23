def solution(n):
    result = [0,1]
    for i in range(2,n+1):
        fib = result[i-2]+result[i-1]
        result.append(fib)
    
    answer = result[n] % 1234567
    return answer