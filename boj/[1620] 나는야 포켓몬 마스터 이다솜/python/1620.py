import sys

num = list(map(int, sys.stdin.readline().strip().split()))

d1 = {}
d2 = {}
for i in range(1, num[0]+1):
    s = sys.stdin.readline().strip()
    d1[s] = i
    d2[i] = s

for i in range(num[1]):
    n = sys.stdin.readline().strip()
    if n.isalpha() :
        print(d1[n])
    else:
        print(d2[int(n)])