def solution(s):
    repeat_cnt, zero_cnt = 0, 0
    
    while(s != "1"):
        zero_cnt += s.count("0")
        s = s.replace("0", '')
        s = format(len(s), 'b')
        repeat_cnt+=1
    
    return [repeat_cnt, zero_cnt]