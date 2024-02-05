def solution(n, left, right):
    arr = []
    
    for i in range(left, right+1):
        x = i % n
        y = i // n
        
        if(x == y):
            arr.append(x+1)
        else:
            max_num = max(x, y)
            if(max_num <= x+y < 2*max_num):
                arr.append(max_num+1)  
            
    return arr
        
    
    