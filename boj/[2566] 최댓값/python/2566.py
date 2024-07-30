import sys

list_1 = []
for i in range(9):
    list_1.append(list(map(int, sys.stdin.readline().rstrip().split())))

dict = {}
max_num = -999
for i in range(9):
    list_max = max(list_1[i])
    if max_num < list_max:
        max_num = list_max
        dict = {}
        dict[list_max] = i

num = 0
line_number = dict[max_num]
for i in range(9):
    if list_1[line_number][i] == max_num:
       num = i
       break 

print(max_num)
print(f'{line_number+1} {num+1}')