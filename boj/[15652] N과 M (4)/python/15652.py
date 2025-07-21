import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())

arr = []
for i in range(1, n+1):
    arr.append(i)

for j in combinations_with_replacement(arr, m):
    for k in j:
        print(k, end=" ")
    print()