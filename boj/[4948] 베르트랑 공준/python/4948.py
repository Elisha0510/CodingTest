import sys
import math

arr = [0 for i in range(2*123456 + 1)]
for i in range(2,2*123456 + 1):
    flag = 0
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0:
            flag = 1
            break
    if not flag:
        arr[i] = 1


while 1:
    cnt = 0
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        cnt += arr[i]
    print(cnt)