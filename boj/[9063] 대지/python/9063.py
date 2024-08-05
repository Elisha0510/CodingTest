import sys

n = int(input())

x = []
y = []
for i in range(n):
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    x.append(l[0])
    y.append(l[1])

rect = (max(x) - min(x)) * (max(y) - min(y))
print(rect)
