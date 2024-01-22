def solution(n):
    i = n+1
    while(i<1000000):
        n_count = format(n, 'b').count("1")
        i_count = format(i, 'b').count("1")
        if(n_count == i_count): break
        i += 1
    return i