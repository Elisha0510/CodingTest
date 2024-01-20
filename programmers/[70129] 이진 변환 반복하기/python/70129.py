def solution(s):
    repeat_cnt, zero_cnt = 0, 0
    
    for i in range(0,10):
        zero_cnt += s.count("0")
        s = s.replace("0", '')
        s = format(len(s), 'b')
        if(s == "1"):
            repeat_cnt = i+1
            break
    
    return [repeat_cnt, zero_cnt]