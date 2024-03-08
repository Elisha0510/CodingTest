arr = []
for i in range(2):
    arr.append(input())


answer = 0
for i in range(len(arr[1])):
    answer += int(arr[1][i])

print(answer)