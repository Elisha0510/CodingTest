import sys

arr = []
avg = 0
for i in range(5):
    n = int(sys.stdin.readline().strip())
    avg += int(n // 5)
    arr.append(n)

arr.sort()

print(avg)
print(arr[2])