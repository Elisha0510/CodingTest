import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())

arr = []
for i in range(1, n+1):
    arr.append(i)

for j in product(arr, repeat=m):
    for k in j:
        print(k, end=" ")
    print()