import sys

n = int(sys.stdin.readline().strip())

d = {}
x_arr = []
for i in range(n):
    p = list(map(int, sys.stdin.readline().strip().split()))
    if p[0] not in d:
        x_arr.append(p[0])
        d[p[0]] = [p[1]]
    else:
        d[p[0]].append(p[1])

x_arr.sort()
    
for key, value in d.items():
    value.sort()

for x in x_arr:
    for y in d[x]:
        print(f"{x} {y}")
