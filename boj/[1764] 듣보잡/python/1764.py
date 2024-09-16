import sys

num = list(map(int, sys.stdin.readline().strip().split()))

arr1 = []
for n in range(num[0]):
    arr1.append(sys.stdin.readline().strip())

arr2 = []
for n in range(num[1]):
    arr2.append(sys.stdin.readline().strip())

answer = list(set(arr1) & set(arr2))
answer.sort()

print(len(answer))
for i in answer:
    print(i)