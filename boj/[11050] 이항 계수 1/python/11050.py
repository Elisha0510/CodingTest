arr = list(map(int,input().split()))

answer = 1
number = arr[0]
for i in range(arr[1]):
    answer *= number
    number -= 1

div = 1
for i in range(1, arr[1]+1):
    div *= i

print(answer//div)