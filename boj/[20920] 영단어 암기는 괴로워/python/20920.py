import sys

n, m = map(int, sys.stdin.readline().strip().split())

d = {}
for i in range(n):
    s = sys.stdin.readline().strip()
    if len(s) >= m and s in d:
        d[s] += 1
    elif len(s) >= m and s not in d:
        d[s] = 1

d = sorted(d.items(), key=lambda x: x[1], reverse=True)
max_num = d[0][1]

arr = []
a = []
for d_element in d:
    if d_element[1] == max_num:
        a.append(d_element[0])
    else:
        arr.append(a)
        max_num = d_element[1]
        a = []
        a.append(d_element[0])
arr.append(a)

answer = []
for a in arr:
    a = sorted(a, key= lambda x: (-len(x), x))
    answer += a


for a in answer:
    print(a)