import sys

n = int(sys.stdin.readline().strip())

d = {}
y_arr = []
for i in range(n):
    p = list(map(int, sys.stdin.readline().strip().split()))
    if p[1] not in d:
        y_arr.append(p[1])
        d[p[1]] = [p[0]]
    else:
        d[p[1]].append(p[0])

y_arr.sort()
    
for key, value in d.items():
    value.sort()

for y in y_arr:
    for x in d[y]:
        print(f"{x} {y}")
