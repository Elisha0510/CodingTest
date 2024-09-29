import sys

qs_cnt = int(sys.stdin.readline().strip())
qs_num = list(map(int, sys.stdin.readline().strip().split()))
first_num = list(map(int, sys.stdin.readline().strip().split()))
input_cnt = int(sys.stdin.readline().strip())
input_num = list(map(int, sys.stdin.readline().strip().split()))

answer = []
for i in range(len(first_num) -1, -1, -1):
    if qs_num[i] == 0:
        answer.append(first_num[i])

answer += input_num

for i in range(input_cnt):
    print(answer[i], end=" ")