import sys

num = list(map(int, sys.stdin.readline().strip().split()))
arr1 = list(map(int, sys.stdin.readline().strip().split()))
arr2 = list(map(int, sys.stdin.readline().strip().split()))

print(len(list(set(arr1) - set(arr2))) + len(list(set(arr2) - set(arr1)))) 
