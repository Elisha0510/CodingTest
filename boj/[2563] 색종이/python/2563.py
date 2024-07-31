import sys

number = int(input())

c = []
for i in range(number):
    c.append(list(map(int, sys.stdin.readline().rstrip().split())))

back = []
for i in range(100):
    back.append([0 for i in range(100)])

for i in range(len(c)):
    for y in range(c[i][1]-1, c[i][1]+9):
        for x in range(c[i][0]-1, c[i][0]+9):
            back[y][x] += 1

cnt = 0
for y in range(100):
    for x in range(100):
        if back[y][x]:
            cnt += 1
        
print(cnt)