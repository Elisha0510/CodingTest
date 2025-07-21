import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

arr = []
for i in range(1, n+1):
    arr.append(i)

for j in permutations(arr, m):
    for k in j:
        print(k, end=" ")
    print()