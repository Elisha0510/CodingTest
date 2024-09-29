import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

arr.sort()

length = len(arr)
if length % 2 == 0:
    print(arr[0] * arr[-1])
else:
    idx = length // 2
    print(arr[idx]**2)