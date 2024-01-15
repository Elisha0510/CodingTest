def solution(start_num, end_num):
    result = []
    sub = start_num - end_num
    for i in range(start_num, end_num-1, -1):
        result.append(i)
    return result
    