import sys

card_num = int(sys.stdin.readline().strip())
card_arr = list(map(int, sys.stdin.readline().strip().split()))

number = int(sys.stdin.readline().strip())
num_arr = list(map(int, sys.stdin.readline().strip().split()))

d = {}
for n in num_arr:
    d[n] = 0

for c in card_arr:
    if c in d:
        d[c] = 1
        
for key, value in d.items():
    print(value, end=" ")