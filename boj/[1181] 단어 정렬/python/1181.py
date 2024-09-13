import sys

n = int(sys.stdin.readline().strip())

arr = []
for i in range(n):
    element = sys.stdin.readline().strip()
    arr.append(element)

arr2 = list(set(arr))

# 2차원 배열 길이로 정렬
arr2.sort(key=len)

max_length = max(arr2[-1])
answer = []
i = 0
flag = 0
while 1:
    arr3 = []
    length = len(arr2[i])
    for j in range(i, len(arr2)+1):
        if j == len(arr2):
            flag = 1
            break
        if length == len(arr2[j]):
            arr3.append(arr2[j])
        elif length < len(arr2[j]):
            i = j
            break
    arr3.sort()
    answer += arr3
    if flag:
        break
    
for a in answer:
    print(a)