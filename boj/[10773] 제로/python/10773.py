import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    number = int(sys.stdin.readline().strip())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))
