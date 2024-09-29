import sys
import math

n = int(sys.stdin.readline().strip())

for i in range(n):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    answer = 0
    if arr[0] >= arr[1]:
        answer = math.comb(arr[0], arr[1])
    else: 
        answer = math.comb(arr[1], arr[0])
    print(answer)