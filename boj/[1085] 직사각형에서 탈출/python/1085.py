import sys

l = list(map(int, sys.stdin.readline().rstrip().split()))

answer = []
answer.append(l[2] - l[0])
answer.append(l[3] - l[1])
answer.append(l[0])
answer.append(l[1])

print(min(answer))
