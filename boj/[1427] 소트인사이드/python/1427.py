import sys

n = list(map(int, sys.stdin.readline().strip()))
n.sort(reverse=True)
s = list(map(str, n))
print(''.join(s))
