import sys
import math

arr = list(map(int, sys.stdin.readline().rstrip().split()))

day = arr[0]
night = arr[1]
height = arr[2]

print(math.ceil(((height - day) / (day - night))) + 1)