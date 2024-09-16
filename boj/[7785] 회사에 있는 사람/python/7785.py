import sys

num = int(sys.stdin.readline().strip())

d = {}
for i in range(num):
    l = list(sys.stdin.readline().strip().split())
    d[l[0]] = l[1]
    if l[1] == "leave":
        del d[l[0]]

arr = sorted(d, reverse=True)

for a in arr:
    print(a)