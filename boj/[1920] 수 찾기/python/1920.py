import sys

n = int(input())
arr = set(map(int, sys.stdin.readline().strip().split()))
m = int(input())
arr2 = list(map(int, sys.stdin.readline().strip().split()))

for a in arr2:
    print(1) if a in arr else print(0)

        