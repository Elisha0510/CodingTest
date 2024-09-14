import sys

n = int(sys.stdin.readline().strip())

d = {}
age = []
for i in range(n):
    l = sys.stdin.readline().strip().split()
    age_num = int(l[0])
    if age_num not in d:
        d[age_num] = [l[1]]
    else:
        d[age_num] += [l[1]]
    if age_num not in age:
        age.append(age_num)

age.sort()

for i in age:
    for j in d[i]:
        print(f"{i} {j}")
        