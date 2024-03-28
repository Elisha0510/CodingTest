def solution(participant, completion):
    h = {}
    
    for i in participant:
        if i not in h:
            h[i] = 1
        else:
            h[i] += 1
    
    for i in completion:
        if i in h:
            h[i] -= 1
    
    for i in h:
        if h[i] == 1:
            return i