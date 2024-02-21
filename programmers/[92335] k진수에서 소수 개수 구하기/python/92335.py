import math

def solution(n, k):
    rArr = []
    while(1):
        r = n % k
        rArr.append(r)
        if(n < k): break
        n = n // k
        
    
    rArr.reverse()
    rArr.append(0)
    
    pArr = []
    p = ''
    for i in range(len(rArr)):
        if rArr[i] == 0 and p != '':
            if(p != '1'):
                pArr.append(p)
            p = ''
        elif rArr[i] != 0 :
            p += str(rArr[i])
        if i == len(rArr)-1 and p != '':
            pArr.append(p)
    
    
    answer = []
    num = 0
    for i in pArr:
        result = isPrime(int(i))
        answer.append(result)
    return answer.count(True)
    
def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if(number % i == 0):
            return False
    return True