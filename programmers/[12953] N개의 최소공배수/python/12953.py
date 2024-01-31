import math
def solution(arr):    
    
    result = arr[0]
    for i in range(1, len(arr)):
        result = result * arr[i] // math.gcd(result, arr[i])
    
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
        
            
            
            