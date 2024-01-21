def solution(n):
    cnt = 0
    num_arr = []
    
    if(n%2 == 1 and n != 1): cnt += 1
    
    for i in range(2, int((n/2)+1)):
        if(n%i == 0): 
            num_arr.append(i)
             
    for i in num_arr:
        if(int(n/i)%2 !=0):
            cnt+=1
    
    return cnt + 1
