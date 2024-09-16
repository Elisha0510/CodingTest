import sys

s = list(sys.stdin.readline().strip())

answer = []
for j in range(1, len(s)+1):
    for i in range(0, len(s)+1-j):
        answer.append(''.join(s[i: i+j]))

print(len(list(set(answer))))