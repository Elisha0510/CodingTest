import sys

l = []
for i in range(5):
    l.append(list(sys.stdin.readline().rstrip()))

max_length = -999
for i in range(5):
    length = len(l[i])
    if max_length < length:
        max_length = length

for i in range(5):
    length = len(l[i])
    for x in range(max_length - length):
        l[i].append(' ')

for x in range(max_length):
    str = ''
    for y in range(5):
        e = l[y][x]
        if e != ' ':
            str += e
    print(str, end='')