import sys

nk = list(map(int, sys.stdin.readline().strip().split()))
arr = list(map(int, sys.stdin.readline().strip().split()))

arr.sort()

idx = nk[0] - nk[1]

print(arr[idx])