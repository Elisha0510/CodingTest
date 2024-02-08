def solution(arr1, arr2):
    y_num = len(arr1)
    x_num = len(arr2[0])
    
    c = [[0 for col in range(x_num)] for row in range(y_num)]
    
    sum = 0
    for y in range(y_num):
        for x in range(x_num):
            for z in range(len(arr2)):
                sum += (arr1[y][z] * arr2[z][x])
            c[y][x] = sum    
            sum = 0   
    return c
        