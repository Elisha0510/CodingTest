def solution(n,a,b):
    
    if(a>b):
        a, b = b, a

    repeat = 0
    for i in range(1, 21):
        if(2**i == n):
            repeat = i
            break
        
    while(1):
        if(a <= (n/2) and b>(n/2)):
            return repeat
        else:
            if(a>(n/2)):
                a-=(n/2)
                b-=(n/2)
            n/=2
            repeat -= 1
                
                

    
    
        

        