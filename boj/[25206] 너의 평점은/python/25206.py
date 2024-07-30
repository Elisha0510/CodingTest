import sys

dict = {'A+':4.5, 'A0':4.0, 'B+': 3.5, 'B0': 3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0': 1.0, 'F': 0.0}

list = []
for i in range(20):
    list.append(sys.stdin.readline().rstrip().split())

sum = 0
total_sum = 0
for i in range(len(list)):
    grade = float(list[i][1])
    avg = list[i][2]
    if avg in dict:
        total_sum += grade * dict[avg]
        sum += grade
    else:
        continue

print(total_sum/sum)