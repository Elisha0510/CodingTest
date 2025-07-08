def make_arr(num):
    arr = []
    for i in range(num):
        a = []
        for j in range(num):
            a.append('*')
        arr.append(a)
    return arr

def make_star(arr, length, row1, col1):

    if length ==1:
        return
    
    step = length // 3

    for i in range(col1+step, col1+2*step):
        for j in range(row1+step, row1+2*step):
            arr[i][j] = ' '
    
    for i in range(col1, length+col1, step):
        for j in range(row1, length+row1, step):
            make_star(arr, step, i, j)

n = int(input())
arr = make_arr(n)
result_arr = make_star(arr, n, 0, 0)


for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()
