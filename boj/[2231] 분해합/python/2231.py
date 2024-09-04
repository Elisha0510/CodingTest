n = int(input())

answer = 0
for i in range(0, n):
    num_str = str(i)
    length = len(num_str)
    sum = 0
    for j in range(0, length):
        sum += int(num_str[j])
    if i + sum == n:
        answer = i
        break

print(answer)