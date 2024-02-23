def solution(n, t, m, p):
    # n 진법에 맞춰 변환
    # 튜브의 순서 구하기
    
    result = '0'
    for i in range(1,t*m):
        result += getNumber(i, n)
    result = result[:t*m]
    
    answer = ''
    for i in range(len(result)):
        if(i % m == p-1):
            answer += result[i]
    
    return answer

def getNumber(i, n):
    dic = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    string = ''
    while (1):
        d = divmod(i, n)
        if(i == d[0]): break
        r = d[1]
        if d[1] in dic.keys():
            r = dic[r]
        string += str(r)
        i = d[0]
    return string[::-1]
    
    
    
    