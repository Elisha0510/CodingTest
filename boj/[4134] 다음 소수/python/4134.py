import sys
import math

n = int(sys.stdin.readline().strip())

for i in range(n):
    answer = 0
    num = int(sys.stdin.readline().strip())
    for i in range(num, (4 * (10 ** 9)) + 10):
        if i < 2:
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            print(i)
            break