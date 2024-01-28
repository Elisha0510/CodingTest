def solution(n):
    cnt = 0 
    return find_minimum(n, cnt)
    
def find_minimum(n, cnt):
    if(n%2 == 0):
        return find_minimum(int(n/2), cnt)
    elif(n%2 == 1 and n != 1):
        cnt += 1
        return find_minimum(n-1, cnt)
    elif(n == 1):
        cnt += 1
        return cnt