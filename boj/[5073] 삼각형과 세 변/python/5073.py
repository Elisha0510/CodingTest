import sys

arr = []
while 1:
    l = list(map(int, sys.stdin.readline().strip().split()))
    if l[0] == 0 and l[1] == 0 and l[2] == 0:
        break
    max_length = max(l)
    arr1 = l[:]
    arr1.remove(max_length)
    if sum(arr1) <= max_length:
        print("Invalid")
    elif l[0] == l[1] and l[1] == l[2] and l[0] == l[2]:
        print("Equilateral")
    elif l[0] != l[1] and l[1] != l[2] and l[0] != l[2]:
        print("Scalene")
    else:
        print("Isosceles")