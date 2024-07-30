import sys

a, b = map(int, input().split())

list_1 = []
for i in range(a):
    list_1.append(list(map(int, sys.stdin.readline().rstrip().split())))

list_2 = []
for i in range(a):
    list_2.append(list(map(int, sys.stdin.readline().rstrip().split())))

answer = []
for y in range(a):
    l = []
    for x in range(b):
        l.append(str(list_1[y][x] + list_2[y][x]))
    answer.append(l)

for i in answer:
    print(" ".join(i))