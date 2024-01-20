def solution(s):
    repeat_cnt = 0
    zero_cnt = 0
    str = s
    for i in range(0,10):
        before = len(str)
        str = str.replace("0", '')
        after = len(str)
        zero_cnt += before - after
        num = len(str)
        str = format(num, 'b')
        if(str == "1"):
            repeat_cnt = i+1
            break
    
    return [repeat_cnt, zero_cnt]