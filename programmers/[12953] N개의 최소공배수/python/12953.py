def solution(arr):    
    mul, answer = 1,1
    for i in arr:
        mul *= i

    result = arr[0]
    for i in range(1, len(arr)):
        g = max_number(result, arr[i])
        result = result * arr[i] / g
    
    return result

def max_number(a, b):
    while(1):
        div = a%b
        if(div == 0):
            break
        else:
            a = b
            b = div
    
    return b
        
            
            
            