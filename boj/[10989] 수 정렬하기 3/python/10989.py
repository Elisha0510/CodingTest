import sys

n = int(sys.stdin.readline().strip())
arr = [0]*10001

for i in range(n):
    num = int(sys.stdin.readline().strip())
    arr[num] += 1

for i in range(1, 10001):
    for j in range(arr[i]):
        print(i)